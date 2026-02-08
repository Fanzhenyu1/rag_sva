import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from pymilvus import connections, MilvusClient, FieldSchema, CollectionSchema, DataType, Collection, AnnSearchRequest, RRFRanker
from pymilvus.model.hybrid import BGEM3EmbeddingFunction

def embedding_model_1():
    embeddings = HuggingFaceEmbeddings(    
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return embeddings

def embedding_model_2(use_fp16=False, device="cpu"):
    embeddings = BGEM3EmbeddingFunction(
                    use_fp16=use_fp16, device=device
    )
    return embeddings

def vectorstore_build(model):
    vectorstore = InMemoryVectorStore(model)
    return vectorstore

def index_build_store(chunks):
    ## load embedding model ##
    embedding_model = embedding_model_1()
    print(f"#### Embedding model has been loaded. ####")

    ## build index of chunks ##
    vector_store = InMemoryVectorStore(embedding_model)
    vector_store.add_documents(chunks)

    print(f"#### Chunks have been added to the vector store. ####")
    return vector_store

def vector_store_new(vector_store: InMemoryVectorStore, new_chunks):
    vector_store.add_documents(new_chunks)
    print(f"#### New chunks have been added to the vector store. ####")
    return vector_store

def vector_store_search(vector_store: InMemoryVectorStore, query: str, k: int = 3):
    results = vector_store.similarity_search(query, k=k)
    print(f"#### Search has been finished. ####")
    return results

def hyper_vector_retrieval(chunks, query, k=3):
    COLLECTION_NAME = "hyper_retrieval_demo"
    MILVUS_URI = "http://localhost:19530"  # 服务器模式    
    print(f"--> 正在连接到 Milvus: {MILVUS_URI}")
    connections.connect(uri=MILVUS_URI)
    print("--> 正在初始化 BGE-M3 嵌入模型...")
    ef = embedding_model_2(use_fp16=False, device="cpu")

    milvus_client = MilvusClient(uri=MILVUS_URI)
    # if milvus_client.has_collection(COLLECTION_NAME):
    #     print(f"--> 正在删除已存在的 Collection '{COLLECTION_NAME}'...")
    #     milvus_client.drop_collection(COLLECTION_NAME)

    fields = [
        FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=True, auto_id=True, max_length=100),
        FieldSchema(name="chunk_text", dtype=DataType.VARCHAR, max_length=4096),
        FieldSchema(name="sparse_vector", dtype=DataType.SPARSE_FLOAT_VECTOR),
        FieldSchema(name="dense_vector", dtype=DataType.FLOAT_VECTOR, dim=ef.dim["dense"])    
    ]
    # 如果集合不存在，则创建它及索引
    if not milvus_client.has_collection(COLLECTION_NAME):
        print(f"--> 正在创建 Collection '{COLLECTION_NAME}'...")
        schema = CollectionSchema(fields, description="混合检索示例")
        # 创建集合
        collection = Collection(name=COLLECTION_NAME, schema=schema, consistency_level="Strong")
        print("--> Collection 创建成功。")
        # 4. 创建索引
        print("--> 正在为新集合创建索引...")
        sparse_index = {"index_type": "SPARSE_INVERTED_INDEX", "metric_type": "IP"}
        collection.create_index("sparse_vector", sparse_index)
        print("稀疏向量索引创建成功。")

        dense_index = {"index_type": "AUTOINDEX", "metric_type": "IP"}
        collection.create_index("dense_vector", dense_index)
        print("密集向量索引创建成功。")
    else:
        print(f"--> Collection '{COLLECTION_NAME}' 已存在，重用索引。")

    collection = Collection(COLLECTION_NAME)

    # 5. 加载数据并插入
    collection.load()
    print(f"--> Collection '{COLLECTION_NAME}' 已加载到内存。")

    if collection.is_empty:
        print(f"--> Collection 为空，开始插入数据...")
        print("--> 正在生成向量嵌入...")
        chunk_texts = [doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in chunks]
        embeddings = ef(chunk_texts)
        print("--> 向量生成完成。")

        # 获取向量
        sparse_vectors = embeddings["sparse"]
        dense_vectors = embeddings["dense"]
        # 插入数据
        print("--> 正在插入数据到 Collection...")
        collection.insert([chunk_texts, sparse_vectors, dense_vectors])
        collection.flush()
        print(f"--> 数据插入完成，总数: {collection.num_entities}")
    else:
        print(f"--> Collection 中已有 {collection.num_entities} 条数据，跳过插入。")

    # 6. 执行混合检索
    print(f"--> 正在执行混合检索...")
    query_embeddings = ef([query])
    dense_vec = query_embeddings["dense"][0]
    sparse_vec = query_embeddings["sparse"]._getrow(0)
    # 定义搜索参数
    search_params = {"metric_type": "IP", "params": {}}

    # 创建 RRF 融合器
    rerank = RRFRanker(k=60)

    # 创建搜索请求
    dense_req = AnnSearchRequest([dense_vec], "dense_vector", search_params, limit=3)
    sparse_req = AnnSearchRequest([sparse_vec], "sparse_vector", search_params, limit=3)

    # 执行混合搜索
    results = collection.hybrid_search(
        [sparse_req, dense_req],
        rerank=rerank,
        limit=3,
        output_fields=["chunk_text"]
    )[0]
    result_list = [hit.entity.get("chunk_text") for hit in results]

    # 7. 清理资源
    milvus_client.release_collection(collection_name=COLLECTION_NAME)
    print(f"已从内存中释放 Collection: '{COLLECTION_NAME}'(保留collection)")
    # milvus_client.drop_collection(COLLECTION_NAME)
    # print(f"已删除 Collection: '{COLLECTION_NAME}'")
    return result_list

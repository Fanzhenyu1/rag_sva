import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from langchain_core.vectorstores import InMemoryVectorStore

from langchain_huggingface import HuggingFaceEmbeddings

from sentence_transformers import SentenceTransformer

def embedding_model_1():
    embeddings = HuggingFaceEmbeddings(    
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return embeddings

def embedding_model_2():
    embeddings = HuggingFaceEmbeddings(
        model_name="Qwen/Qwen3-Embedding-8B",
        model_kwargs={'device': 'cuda'}
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

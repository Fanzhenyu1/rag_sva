import os
import file_load
import doc_chunk
import vector_store
import prompt_build
from langchain_deepseek import ChatDeepSeek
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document

def format_docs(docs):
    """
    将检索到的文档列表格式化为一个字符串，用作上下文人。
    
    Args:
        docs (List[Document]): 检索到的文档列表。
        
    Returns:
        str: 格式化后的上下文字符串。
    """
    return "\n\n".join(doc.page_content for doc in docs)

def make_documents(text):
    return [Document(page_content=text)]

def my_chain(
        bm_enable: int = 1,
        design_name: str = "aes",
        RAG_ENABLE: int = 1
):

########################=====source files directory=====############################
####################################################################################
    if bm_enable == 1:
        # dir of benchmark data
        bm_path = f"e:/mylife_yanjiu/project/rag_sva/benchmark/{design_name}"
    # dir of SPEC
    src_path = f"e:/mylife_yanjiu/project/rag_sva/src/{design_name}"
    spec_path = src_path + "/spec"
    spec_file = [
        os.path.normpath(os.path.join(spec_path, f))
        for f in os.listdir(spec_path)
        if os.path.isfile(os.path.join(spec_path, f)) and f.lower().endswith(('.md'))
    ]

    print(f"SPEC file: {spec_file}")
    all_files = spec_file
    # dir of temp files
    temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/"

########################=====query to RAG=====######################################
####################################################################################
    pass

    with open('e:/mylife_yanjiu/project/rag_sva/rules/asset_identify_en.md', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    custom_rag_prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "documents"]
    )
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    combine_docs_chain = create_stuff_documents_chain(llm, custom_rag_prompt)

    embedding = vector_store.embedding_model_1()
    vec_store = vector_store.vectorstore_build(embedding)

    lib_data_file = ["e:/mylife_yanjiu/project/rag_sva/lib_data/output.md"]
    docs = file_load.load_files(lib_data_file) # load lib data
    chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
    vec_store.add_documents(chunks) # build vector store
    retriever = vec_store.as_retriever()

    def retrieve_docs(input_dict):
        if RAG_ENABLE != 1:
            return []
        else:
            query = input_dict.get("input", "") # 从输入中获取查询
            retrieved_docs = retriever.invoke(query) # 执行检索
            # docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:5]])
            return retrieved_docs[:5]

    custom_rag_chain = (
        RunnablePassthrough()
        | RunnablePassthrough.assign(context=retrieve_docs) # 执行检索，结果赋给"context"
        # | RunnablePassthrough.assign(documents=lambda x: x.get("documents", "")) # 直接传递外部提供的"documents"
        | RunnablePassthrough.assign(documents=lambda x: make_documents(x.get("documents", "")))
        | combine_docs_chain # 将 "context" 和 "documents" 传递给文档组合链
    )

    return custom_rag_chain



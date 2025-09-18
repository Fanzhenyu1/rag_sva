import os
import file_load
import doc_chunk
import vector_store
import prompt_build
from langchain_deepseek import ChatDeepSeek

def answer_to_temp(answer, temp_path, filename="1111.txt"):
    os.makedirs(temp_path, exist_ok=True)
    file_path = os.path.join(temp_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(answer)
    print(f"Answer saved to {file_path}")
    return file_path

def design_analysis_llm_call(rtl_files, docs_content, RAG_ENABLE=0):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_design_analysis(docs_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_design_analysis("", rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串

def query_simplify_llm_call(answer_design, docs_content, RAG_ENABLE=0):
    # build full prompt
    filled_prompt = prompt_build.prompt_build_query_simplify("", answer_design, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串
    
def comment_llm_call(rtl_files, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_comment_fill(docs_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_comment_fill("", rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=8192,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串

def asset_llm_call(rtl_files, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_assets_identify(docs_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_assets_identify("", rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串

def testpoint_llm_call(rtl_files, asset_content, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_testpoint_generation(docs_content, asset_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_testpoint_generation("", asset_content, rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串

def property_llm_call(rtl_files, testpoint_content, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_property_generation(docs_content, testpoint_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_property_generation("", testpoint_content, rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串

def main():

    RAG_ENABLE = 1
    design_name = "aes"  # 设计名称
    # dir of src
    src_path = f"e:/mylife_yanjiu/project/rag_sva/src/{design_name}"
    rtl_files = [
        os.path.normpath(os.path.join(src_path, f))
        for f in os.listdir(src_path)
        if os.path.isfile(os.path.join(src_path, f)) and f.lower().endswith(('.v', '.sv', 'txt', '.vhd'))
    ]
    # dir of SPEC
    spec_path = src_path + "/spec"
    spec_file = [
        os.path.normpath(os.path.join(spec_path, f))
        for f in os.listdir(spec_path)
        if os.path.isfile(os.path.join(spec_path, f)) and f.lower().endswith(('.md'))
    ]
    print(f"RTL file: {rtl_files}")
    print(f"SPEC file: {spec_file}")
    all_files = rtl_files + spec_file
    # dir of temp files
    temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/"

####################################################################################
####################################################################################
    if(0):
        # LLM call for design analysis
        answer_design = design_analysis_llm_call(all_files, "", 0)
        # save answer to temp file
        answer_to_temp(answer_design, temp_path, "answer_design.txt")
        pass

        # with open(os.path.join(temp_path, "answer_design.txt"), "r", encoding="utf-8") as f:
        #     answer_design = f.read()            # 一般需要注释掉
        # query_simplify
        query_rag = query_simplify_llm_call(answer_design, "", 0)
        # save query to temp file
        answer_to_temp(query_rag, temp_path, "query_rag.txt")
        pass
########################=====query to RAG=====######################################
####################################################################################
    lib_path = "e:/mylife_yanjiu/project/rag_sva/lib_data"
    lib_data_file = [lib_path + "/output.md"]

    with open(os.path.join(temp_path, "query_rag.txt"), "r", encoding="utf-8") as f:
        query_rag = f.read()            # 一般需要注释掉
    docs = file_load.load_files(lib_data_file) # load lib data
    chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
    vec_store = vector_store.index_build_store(chunks) # build vector store
    retrieved_docs = vector_store.vector_store_search(vec_store, query_rag)
    docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:5]])
    print(f"Retrieved documents:\n{docs_content}\n")
    pass

########################=====LLM With RAG=====######################################
####################################################################################

    # LLM call for comment fill
    answer_comment = comment_llm_call(all_files, docs_content if RAG_ENABLE == 1 else "", 0)
    # save answer to temp file
    answer_to_temp(answer_comment, temp_path, "answer_comment.txt")
    all_files = rtl_files + [os.path.join(temp_path, "answer_comment.txt")]

    # LLM call for asset identify
    answer_asset = asset_llm_call(all_files, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_asset, temp_path, "answer_asset.txt")

    # LLM call for testpoint generation
    answer_testpoint = testpoint_llm_call(all_files, answer_asset, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_testpoint, temp_path, "answer_testpoint.txt")

    # LLM call for property generation
    answer_property = property_llm_call(rtl_files, answer_testpoint, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_property, temp_path, "answer_property.txt")
    return 0

if __name__ == "__main__":
    main()

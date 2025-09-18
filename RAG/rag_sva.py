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

def design_analysis_llm_call(rtl_files, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_design_analysis(docs_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_design_analysis("", rtl_files, RAG_ENABLE)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.7,
        max_tokens=2048,
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
        max_tokens=2048,
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
        max_tokens=2048,
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
        max_tokens=2048,
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


    if RAG_ENABLE == 1:
        # load files
        dir_path = "e:/mylife_yanjiu/project/rag_sva/lib_data"
        # file_paths = [
        #     os.path.join(dir_path, f)
        #     for f in os.listdir(dir_path)
        #     if os.path.isfile(os.path.join(dir_path, f))
        # ]
        file_paths = spec_file + ["e:/mylife_yanjiu/project/rag_sva/lib_data/公开信息收集的SoC漏洞数据.md",
                                  "e:/mylife_yanjiu/project/rag_sva/lib_data/output.md"]
        print(f"Source document files: {file_paths}")
        docs = file_load.load_files(file_paths)

        # file content chunking
        chunks = doc_chunk.langchain_doc_chunk(docs)

        # build index of chunks & store in vector store
        vec_store = vector_store.index_build_store(chunks)

        # search document
        query = "UART design have important access control requirments, memory ranges of UART should not be overlap with other IPs. Please search related information from the documents."
        retrieved_docs = vector_store.vector_store_search(vec_store, query)
        docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:2]])
        print(f"Retrieved documents:\n{docs_content}\n")
        pass
        # for i, doc in enumerate(retrieved_docs):
        #     print(f"Document {i+1}:\n{doc.page_content}\n")

    # LLM call for design analysis
    answer_design = design_analysis_llm_call(all_files, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_design, temp_path, "answer_design.txt")
    pass

    # LLM call for asset identify
    answer_asset = asset_llm_call(rtl_files, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_asset, temp_path, "answer_asset.txt")

    # LLM call for testpoint generation
    answer_testpoint = testpoint_llm_call(rtl_files, answer_asset, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_testpoint, temp_path, "answer_testpoint.txt")

    # LLM call for property generation
    answer_property = property_llm_call(rtl_files, answer_testpoint, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_property, temp_path, "answer_property.txt")

    return answer_property

if __name__ == "__main__":
    main()

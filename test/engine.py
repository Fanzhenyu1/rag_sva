import os
import argparse
import sys
sys.path.append(r"e:\mylife_yanjiu\project\rag_sva\RAG")
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

def llm_call(rtl_files, docs_content, RAG_ENABLE, rule="", asset_content="", testpoint_content="", sva_content=""):
    #### rule identify ####
    if rule == "asset":
        filled_prompt = prompt_build.prompt_build_assets_identify(docs_content if RAG_ENABLE==1 else "", rtl_files, RAG_ENABLE)
    if rule == "testpoint":
        filled_prompt = prompt_build.prompt_build_testpoint_generation(docs_content if RAG_ENABLE==1 else "", asset_content, rtl_files, RAG_ENABLE)
    if rule == "property":
        filled_prompt = prompt_build.prompt_build_property_generation(docs_content if RAG_ENABLE==1 else "", testpoint_content, rtl_files, RAG_ENABLE)
    if rule == "simplify":
        filled_prompt = prompt_build.prompt_build_sva_simplify(sva_content)
    if rule == "query":
        filled_prompt = prompt_build.prompt_build_query_simplify("", rtl_files, RAG_ENABLE)
    if rule == "property_all":
        filled_prompt = prompt_build.prompt_build_property_generation_all(docs_content if RAG_ENABLE==1 else "", rtl_files, RAG_ENABLE)

    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.4,
        max_tokens=4096,
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    answer = llm.invoke(filled_prompt)
    if hasattr(answer, 'content'):  # 检查是否有content属性
        return answer.content
    elif isinstance(answer, str):   # 如果是str直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串    

def my_chain(BM_ENABLE, design_name, RAG_ENABLE):

    #### source files directory ####
    if BM_ENABLE == 1:
        src_path = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/src"
        if (0):  #### choose dut or dut_buggy ####
            rtl_files = [src_path + "/dut.sv"]
        else:
            rtl_files = [src_path + "/dut_buggy.sv"]
        temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/"
    else:
        src_path = f"e:/mylife_yanjiu/project/rag_sva/src/{design_name}"
        rtl_files = [
            os.path.normpath(os.path.join(src_path, f))
            for f in os.listdir(src_path)
            if os.path.isfile(os.path.join(src_path, f)) and f.lower().endswith(('.v', '.sv', 'txt', '.vhd'))
        ]
        temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/common_temp/{design_name}/"
    print(f"RTL files have been loaded: {rtl_files}")
    print(f"Temp files has been set to temp path: {temp_path}")
####################################################################################
####################################################################################
    if(0):
        # with open(os.path.join(temp_path, "answer_design.txt"), "r", encoding="utf-8") as f:
        #     answer_design = f.read()            # 一般需要注释掉
        # query_simplify
        query_rag = llm_call(rtl_files, "", 0, rule="query")
        # save query to temp file
        answer_to_temp(query_rag, temp_path, "query_rag.txt")
        pass

    #### documents_retrieval ####
    if(1):
        lib_path = "e:/mylife_yanjiu/project/rag_sva/lib_data"
        lib_data_file = [lib_path + "/secdoc_2.md", lib_path + "/output.md"]
        #### query define ####
        with open(os.path.join(temp_path, "query_rag.txt"), "r", encoding="utf-8") as f:
            query_rag = f.read()            # 一般需要注释掉
        ######################
        docs = file_load.load_files(lib_data_file) # load lib data
        chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
        if(0):
            chunks_texts = [doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in chunks]
            pass
            retrieved_docs = vector_store.hyper_vector_retrieval(chunks_texts, query_rag, k=3)    # parmeter k is important
            docs_content = "\n\n".join([doc for doc in retrieved_docs[:3]])
            print(f"Retrieved documents:\n{docs_content}\n")
            answer_to_temp(docs_content, temp_path, "retrived_docs_hyp_0.txt")
        else:
            vec_store = vector_store.index_build_store(chunks) # build vector store
            retrieved_docs = vector_store.vector_store_search(vec_store, query_rag, k=3)    # parmeter k is important
            docs_list = [doc.page_content for doc in retrieved_docs[:3]]
            docs_content = "\n\n".join(docs_list)
            # docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:5]])
            print(f"Retrieved documents:\n{docs_content}\n")
            answer_to_temp(docs_content, temp_path, "retrived_docs_1.txt")
    else:  #### self-defined documents retrieved ####
        docs_content = '''A simple register lock module. "threat model": ["The register (named data) cannot be modified when the lock signal is on."]. "security property": "at every positive edge of clock, the value of the data register is same as its value in the previous clock cycle if the value of the lock signal in the previous clock cycle is 1".'''
        pass

    if(1):
        #### LLM_chain ####
        # LLM call for asset identify
        answer_asset = llm_call(rtl_files, docs_content, RAG_ENABLE, "asset")
        # save answer to temp file
        answer_to_temp(answer_asset, temp_path, "answer_asset_1.txt")
        pass
        # LLM call for testpoint generation
        answer_testpoint = llm_call(rtl_files, docs_content, RAG_ENABLE, "testpoint", asset_content = answer_asset)
        # save answer to temp file
        answer_to_temp(answer_testpoint, temp_path, "answer_testpoint_1.txt")
        pass
        # LLM call for property generation
        answer_property = llm_call(rtl_files, docs_content, RAG_ENABLE, "property", testpoint_content = answer_testpoint)
        answer_to_temp(answer_property, temp_path, "answer_property_1.txt")   
        pass
        # # LLM call for SVA simplify
        # answer_sva_simplify = llm_call("", "", RAG_ENABLE, rule="simplify", sva_content = answer_property)
        # # save answer to temp file
        # answer_to_temp(answer_sva_simplify, temp_path, "answer_finial.txt")
    else:
        # LLM call for property generation all
        answer_property = llm_call(rtl_files, docs_content, RAG_ENABLE, "property_all")
        # save answer to temp file
        answer_to_temp(answer_property, temp_path, "answer_property_all.txt")          



    return 0  

def main():
    parser = argparse.ArgumentParser(description='RAG-SVA')
    parser.add_argument('-b', type=int, default=0, help='benchmark enable')
    parser.add_argument('-d', type=str, help='design name')
    parser.add_argument('-r', type=int, default=0, help='RAG enable')
    parser.add_argument('--help_info', action='help', help='show this help message and exit')
    args = parser.parse_args()

    
    #### design_name check ####
    if not args.d or args.d == "":
        print("Error: design_name is required.")
        print("Use --help_info/-h to see usage.")
        return

    my_chain(args.b, args.d, args.r)

if __name__ == '__main__':
    main()
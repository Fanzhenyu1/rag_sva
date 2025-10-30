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
    elif isinstance(answer, str):   # 如果是str直接返回字符串
        return answer
    else:  # 其他格式的处理
        return str(answer)  # 转换为字符串    

def my_chain(BM_ENABLE, design_name, RAG_ENABLE):

    #### source files directory ####
    if BM_ENABLE == 1:
        src_path = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/src"
        if (1):  #### choose dut or dut_buggy ####
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

    #### documents_retrieval ####
    if(0):
        lib_path = "e:/mylife_yanjiu/project/rag_sva/lib_data"
        lib_data_file = [lib_path + "/output.md"]
        #### query define ####
        with open(os.path.join(temp_path, "query_rag.txt"), "r", encoding="utf-8") as f:
            query_rag = f.read()            # 一般需要注释掉
        ######################
        docs = file_load.load_files(lib_data_file) # load lib data
        chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
        vec_store = vector_store.index_build_store(chunks) # build vector store
        retrieved_docs = vector_store.vector_store_search(vec_store, query_rag, k=5)    # parmeter k is important
        docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:5]])
    else:  #### self-defined documents retrieved ####
        # docs_content = '''
        # HT1:When this operation is completed and the working mode is ECB mode and encryption mode, the Trojan enable counter accumulates. When the Trojan enable counter reaches the threshold predefined by the attacker, the Trojan enable signal (Tj_En) activates the load circuit, which will mask the original output data and lock the output.
        # HT2:When the trigger circuit detects that the input data is a specific value set by the attacker, the hardware Trojan is triggered, and the load circuit will replace this input data with another data with the same bit width, resulting in an error in the operation result of the AES IP.
        # HT3:When the trigger circuit detects that the plaintext length of the input exceeds the attacker's set value, the hardware Trojan is triggered. The Trojan enable signal (Tj_En) is high, causing the last bit of the written data to be inverted, thereby tampering with the value of the written data and resulting in an AES IP encryption error.
        # HT4:When the trigger circuit detects that the plaintext length of this input is equal to the value preset by the attacker, the hardware Trojan is triggered, and the Trojan enable signal (Tj_En) is high, causing the output data to be replaced with the data in the key register. Attackers can illegally obtain keys by listening to the output signals of AES IP, resulting in the destruction of the confidentiality of AES IP.
        # BUG1:This was caused by the incorrect connection between the clock port of the top-level module of AES IP and the clock port of the working mode configuration module. When the AES IP is called by the system to complete the encryption and decryption tasks, the interrupt signal remains zero, and when the host reads the operation result of the AES IP, the read data signal is also zero.
        # BUG2:It is caused by the incorrect setting of the number of rounds for encryption and decryption operations in the finite state machine. For the AES encryption and decryption algorithm with a key length of 128 bits, the finite state critical control data processing unit completes 10 rounds of round transformation. Here, the threshold of the counter is changed to 9 rounds, resulting in the operation ending prematurely.
        # BUG3:Because the mode selection port of the AES IP working mode configuration module is not correctly connected to the mode selection port of the control unit, when the AES IP performs encryption operations, the mode selection signal transmitted to the control unit is in decryption mode, which makes the encryption function of the AES IP unable to be correctly invoked.
        # '''
        docs_content = "A simple register lock module. The register (named data) cannot be modified when the lock signal is on"
        # docs_content = '''A simple traffic controller. Traffic changes from red -> green -> yellow -> red. If a pedestrian presses walk button, traffic should stop for 4 cycles.  "bug description": ["Traffic controller skips yellow before going red when walk button is pressed on green"]'''
    pass
    print(f"Retrieved documents:\n{docs_content}\n")
    answer_to_temp(docs_content, temp_path, "retrived_docs.txt")

    #### LLM_chain ####
    # LLM call for asset identify
    answer_asset = llm_call(rtl_files, docs_content, RAG_ENABLE, "asset")
    # save answer to temp file
    answer_to_temp(answer_asset, temp_path, "answer_asset.txt")

    # LLM call for testpoint generation
    answer_testpoint = llm_call(rtl_files, docs_content, RAG_ENABLE, "testpoint", asset_content = answer_asset)
    # save answer to temp file
    answer_to_temp(answer_testpoint, temp_path, "answer_testpoint.txt")

    # LLM call for property generation
    answer_property = llm_call(rtl_files, docs_content, RAG_ENABLE, "property", testpoint_content = answer_testpoint)
    # save answer to temp file
    answer_to_temp(answer_property, temp_path, "answer_property.txt")  

    # LLM call for SVA simplify
    answer_sva_simplify = llm_call("", "", RAG_ENABLE, rule="simplify", sva_content = answer_property)
    # save answer to temp file
    answer_to_temp(answer_sva_simplify, temp_path, "answer_finial.txt")

    return 0  

def main():
    parser = argparse.ArgumentParser(description='RAG-SVA')
    parser.add_argument('--bm_enable', type=int, default=0, help='benchmark enable')
    parser.add_argument('--design_name', type=str, help='design name')
    parser.add_argument('--rag_enable', type=int, default=0, help='RAG enable')
    parser.add_argument('--help_info', action='help', help='show this help message and exit')
    args = parser.parse_args()

    
    #### design_name check ####
    if not args.design_name or args.design_name == "":
        print("Error: design_name is required.")
        print("Use --help_info/-h to see usage.")
        return

    my_chain(args.bm_enable, args.design_name, args.rag_enable)

if __name__ == '__main__':
    main()
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

def property_llm_call_all(rtl_files, docs_content, RAG_ENABLE):
    # build full prompt
    if RAG_ENABLE == 1:
        filled_prompt = prompt_build.prompt_build_property_generation_all(docs_content, rtl_files, RAG_ENABLE)
    else:
        filled_prompt = prompt_build.prompt_build_property_generation_all("", rtl_files, RAG_ENABLE)
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

def main():

    RAG_ENABLE = 1
    design_name = "aes"  # 设计名称
    # dir of src
    src_path = f"e:/mylife_yanjiu/project/rag_sva/src/{design_name}"
    # rtl_files = [
    #     os.path.normpath(os.path.join(src_path, f))
    #     for f in os.listdir(src_path)
    #     if os.path.isfile(os.path.join(src_path, f)) and f.lower().endswith(('.v', '.sv', 'txt', '.vhd'))
    # ]
    rtl_files = ["e:/mylife_yanjiu/project/aes_ip/AES_bug_in/AES_IP_AXI_interface.sv"]
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
    if(1):
        lib_path = "e:/mylife_yanjiu/project/rag_sva/lib_data"
        lib_data_file = [lib_path + "/secdoc_2.md"]

        with open(os.path.join(temp_path, "query_rag.txt"), "r", encoding="utf-8") as f:
            query_rag = f.read()            # 一般需要注释掉
        docs = file_load.load_files(lib_data_file) # load lib data
        chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
        chunks_texts = [doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in chunks]
        pass
        retrieved_docs = vector_store.hyper_vector_retrieval(chunks_texts, query_rag, k=5)    # parmeter k is important
        docs_content = "\n\n".join([doc for doc in retrieved_docs[:5]])
        print(f"Retrieved documents:\n{docs_content}\n")
        pass
    else:
        docs_content = '''
        HT1:When this operation is completed and the working mode is ECB mode and encryption mode, the Trojan enable counter accumulates. When the Trojan enable counter reaches the threshold predefined by the attacker, the Trojan enable signal (Tj_En) activates the load circuit, which will mask the original output data and lock the output.
        HT2:When the trigger circuit detects that the input data is a specific value set by the attacker, the hardware Trojan is triggered, and the load circuit will replace this input data with another data with the same bit width, resulting in an error in the operation result of the AES IP.
        HT3:When the trigger circuit detects that the plaintext length of the input exceeds the attacker's set value, the hardware Trojan is triggered. The Trojan enable signal (Tj_En) is high, causing the last bit of the written data to be inverted, thereby tampering with the value of the written data and resulting in an AES IP encryption error.
        HT4:When the trigger circuit detects that the plaintext length of this input is equal to the value preset by the attacker, the hardware Trojan is triggered, and the Trojan enable signal (Tj_En) is high, causing the output data to be replaced with the data in the key register. Attackers can illegally obtain keys by listening to the output signals of AES IP, resulting in the destruction of the confidentiality of AES IP.
        BUG1:This was caused by the incorrect connection between the clock port of the top-level module of AES IP and the clock port of the working mode configuration module. When the AES IP is called by the system to complete the encryption and decryption tasks, the interrupt signal remains zero, and when the host reads the operation result of the AES IP, the read data signal is also zero.
        BUG2:It is caused by the incorrect setting of the number of rounds for encryption and decryption operations in the finite state machine. For the AES encryption and decryption algorithm with a key length of 128 bits, the finite state critical control data processing unit completes 10 rounds of round transformation. Here, the threshold of the counter is changed to 9 rounds, resulting in the operation ending prematurely.
        BUG3:Because the mode selection port of the AES IP working mode configuration module is not correctly connected to the mode selection port of the control unit, when the AES IP performs encryption operations, the mode selection signal transmitted to the control unit is in decryption mode, which makes the encryption function of the AES IP unable to be correctly invoked.
        BUG4:When the AES IP is in operation and the operation has not yet been completed, if a read data request from the host is received, the AXI interface will respond to the request and write the output data of the data processing unit (invalid operation intermediate data) to the read cache module, and output these intermediate data, resulting in the destruction of the confidentiality of the AES IP.
        BUG5:Since the reset port of the read cache module in the AXI interface is directly assigned to 1, the internal data of the read cache module will not be cleared when it is reset. Attackers can exploit this vulnerability to illegally read the results of the previous encryption and decryption operations after a reset.
        BUG6:When AESIP is in decryption mode, the shift register in the read cache module is output in an incorrect way, resulting in a decryption error.
        '''

########################=====LLM With RAG=====######################################
####################################################################################

    # LLM call for comment fill
    answer_comment = comment_llm_call(rtl_files, docs_content if RAG_ENABLE == 1 else "", 0)
    # save answer to temp file
    answer_to_temp(answer_comment, temp_path, "answer_comment.txt")

    all_files = rtl_files + [os.path.join(temp_path, "answer_comment.txt")]

    # LLM call for property generation
    answer_property = property_llm_call_all(all_files, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_property, temp_path, "answer_property_all.txt")

    return answer_property

if __name__ == "__main__":
    main()

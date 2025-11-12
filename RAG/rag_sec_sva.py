import os
import openai
import file_load
import doc_chunk
import vector_store
import prompt_build
import json
from pathlib import Path
from dotenv import load_dotenv
from ragas import evaluate
from datasets import Dataset
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall, answer_correctness
from langchain_deepseek import ChatDeepSeek

#### Environment Setup ####
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url_from_env = os.getenv("OPENAI_BASE_URL")
default_base_url = "OPENAI_BASE_URL" # 您常用的 URL 作为默认值
base_url = base_url_from_env if base_url_from_env else default_base_url
print(f"使用的 Base URL: {base_url}")

###################
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY in environment and no fallback provided.")
# 将值写回环境，确保其它库（基于 env 的）也能读取到
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_BASE_URL"] = base_url

# 同时设置 openai 客户端的全局配置（部分库直接使用 openai.api_*）
openai.api_key = api_key
# openai.api_base 是 openai-python 用来覆盖默认 host 的变量（确保格式如 https://your-host/v1）
openai.api_base = base_url


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
        return answer.content, filled_prompt
    elif isinstance(answer, str):   # 如果是直接返回字符串
        return answer, filled_prompt
    else:  # 其他格式的处理
        return str(answer), filled_prompt  # 转换为字符串

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
    
def evaluator_llm_call(input_query, llm_answer, retrived_doc, golden_answer):
    query_list = [input_query]
    answer_list = [llm_answer]
    retrived_list = [retrived_doc]
    golden_list = [golden_answer]

    data_dict = {
        'question': query_list,
        'answer': answer_list,
        'contexts': retrived_list,
        'ground_truth': golden_list
    }
    dataset = Dataset.from_dict(data_dict)

    end_to_end_results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall, answer_correctness]
    )

    print(end_to_end_results)

    return 0

def main():

    RAG_ENABLE = 1
    design_name = "6"  # 设计名称
    # dir of src
    # src_path = f"e:/mylife_yanjiu/project/rag_sva/src/{design_name}"
    bm_path = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}"
    src_path = bm_path + "/src/"

    # rtl_files = [
    #     os.path.normpath(os.path.join(src_path, f))
    #     for f in os.listdir(src_path)
    #     if os.path.isfile(os.path.join(src_path, f)) and f.lower().endswith(('.v', '.sv', 'txt', '.vhd'))
    # ]
    rtl_files = [src_path + "dut_buggy.sv"]

    # # dir of SPEC
    # spec_path = src_path + "/spec"
    # spec_file = [
    #     os.path.normpath(os.path.join(spec_path, f))
    #     for f in os.listdir(spec_path)
    #     if os.path.isfile(os.path.join(spec_path, f)) and f.lower().endswith(('.md'))
    # ]
    print(f"RTL file: {rtl_files}")
    # print(f"SPEC file: {spec_file}")

    # dir of temp files
    temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/"

    # LLM call for comment fill
    answer_comment = comment_llm_call(rtl_files, "", 0)
    # save answer to temp file
    answer_to_temp(answer_comment, temp_path, "answer_comment.txt")
    pass

####################################################################################
####################################################################################
    if(0):
        # LLM call for design analysis
        answer_design = design_analysis_llm_call(rtl_files, "", 0)
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
        lib_data_file = [lib_path + "/output.md"]

        with open(os.path.join(temp_path, "query_rag.txt"), "r", encoding="utf-8") as f:
            query_rag = f.read()            # 一般需要注释掉
        docs = file_load.load_files(lib_data_file) # load lib data
        chunks = doc_chunk.langchain_doc_chunk(docs) # chunking
        vec_store = vector_store.index_build_store(chunks) # build vector store
        retrieved_docs = vector_store.vector_store_search(vec_store, query_rag, k=5)    # parmeter k is important
        docs_list = [doc.page_content for doc in retrieved_docs[:5]]
        docs_content = "\n\n".join(docs_list)
        # docs_content = "\n\n".join([doc.page_content for doc in retrieved_docs[:5]])
        print(f"Retrieved documents:\n{docs_content}\n")
    else:
        docs_content = '''
        HT1:When this operation is completed and the working mode is ECB mode and encryption mode, the Trojan enable counter accumulates. When the Trojan enable counter reaches the threshold predefined by the attacker, the Trojan enable signal (Tj_En) activates the load circuit, which will mask the original output data and lock the output.
        HT2:When the trigger circuit detects that the input data is a specific value set by the attacker, the hardware Trojan is triggered, and the load circuit will replace this input data with another data with the same bit width, resulting in an error in the operation result of the AES IP.
        HT3:When the trigger circuit detects that the plaintext length of the input exceeds the attacker's set value, the hardware Trojan is triggered. The Trojan enable signal (Tj_En) is high, causing the last bit of the written data to be inverted, thereby tampering with the value of the written data and resulting in an AES IP encryption error.
        HT4:When the trigger circuit detects that the plaintext length of this input is equal to the value preset by the attacker, the hardware Trojan is triggered, and the Trojan enable signal (Tj_En) is high, causing the output data to be replaced with the data in the key register. Attackers can illegally obtain keys by listening to the output signals of AES IP, resulting in the destruction of the confidentiality of AES IP.
        BUG1:This was caused by the incorrect connection between the clock port of the top-level module of AES IP and the clock port of the working mode configuration module. When the AES IP is called by the system to complete the encryption and decryption tasks, the interrupt signal remains zero, and when the host reads the operation result of the AES IP, the read data signal is also zero.
        BUG2:It is caused by the incorrect setting of the number of rounds for encryption and decryption operations in the finite state machine. For the AES encryption and decryption algorithm with a key length of 128 bits, the finite state critical control data processing unit completes 10 rounds of round transformation. Here, the threshold of the counter is changed to 9 rounds, resulting in the operation ending prematurely.
        BUG3:Because the mode selection port of the AES IP working mode configuration module is not correctly connected to the mode selection port of the control unit, when the AES IP performs encryption operations, the mode selection signal transmitted to the control unit is in decryption mode, which makes the encryption function of the AES IP unable to be correctly invoked.
        '''
    pass

########################=====LLM With RAG=====######################################
####################################################################################

    all_files = rtl_files + [os.path.join(temp_path, "answer_comment.txt")]

    # LLM call for asset identify
    answer_asset, prompt_asset = asset_llm_call(all_files, docs_content if RAG_ENABLE == 1 else "", RAG_ENABLE)
    # save answer to temp file
    answer_to_temp(answer_asset, temp_path, "answer_asset.txt")
    pass
    evaluator_llm_call(
        prompt_asset,
        answer_asset,
        docs_list,
        open(f"{bm_path}/golden_answer/golden_asset.txt", 'r', encoding='utf-8').read()
    )
    pass

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

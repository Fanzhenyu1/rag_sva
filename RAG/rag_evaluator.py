import os
import openai
import prompt_build
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

# 将值写回环境，确保其它库（基于 env 的）也能读取到
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_BASE_URL"] = base_url

# 同时设置 openai 客户端的全局配置（部分库直接使用 openai.api_*）
openai.api_key = api_key
# openai.api_base 是 openai-python 用来覆盖默认 host 的变量（确保格式如 https://your-host/v1）
openai.api_base = base_url

def get_golden_answer(design_name):
    golden_answer_dir = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/golden_answer/"
    with open(golden_answer_dir + "golden_asset.txt", "r", encoding="utf-8") as f:
        golden_answer = f.read().strip()
    return golden_answer

def get_answer(design_name, outtype):
    answer_dir = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/"
    # with open(answer_dir + "answer_asset_hyp.txt", "r", encoding="utf-8") as f:
    with open(answer_dir + f"answer_asset_{outtype}.txt", "r", encoding="utf-8") as f:
        llm_answer = f.read().strip()
    return llm_answer
def get_retrived_doc(design_name, outtype):
    retrived_doc_dir = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/"
    with open(retrived_doc_dir + f"retrived_docs_{outtype}.txt", "r", encoding="utf-8") as f:
        retrived_doc = f.read()
    retrived_doc_list = [ln for ln in retrived_doc.splitlines() if ln.strip()]
    return retrived_doc_list

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
        metrics=[faithfulness, answer_relevancy, context_recall, answer_correctness]
    )

    print(end_to_end_results)

    return 0

def main():
    design_name = "9"
    BM_ENABLE = 1
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

    if (0):
        outtype = "hyp"
    else:
        outtype = "n"
    #### evaluator call ####
    prompt_all = prompt_build.prompt_build_assets_identify("", rtl_files, 0)
    llm_answer = get_answer(design_name, outtype)
    golden_answer = get_golden_answer(design_name)    
    retrived_doc_list = get_retrived_doc(design_name, outtype)
    pass
    evaluator_llm_call(
        prompt_all,
        llm_answer,
        retrived_doc_list,
        golden_answer
    )
    return 0

if __name__ == "__main__":
    main()
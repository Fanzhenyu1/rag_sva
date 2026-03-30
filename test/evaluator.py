import os
import openai
import json
from pathlib import Path
from dotenv import load_dotenv
from ragas import evaluate
from datasets import Dataset
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

design_name = "0"

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

#### 定义单个样本的数据结构
def create_sample(question, answer, contexts, ground_truth):
    sample = {
        'question': question,
        'answer': answer,
        'contexts': contexts,
        'ground_truth': ground_truth,
        'get_sample_type': 'single'
    }

    return sample

def load_info_json(path: str = r"e:\mylife_yanjiu\project\rag_sva\benchmarks\info.json") -> dict:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def get_design_description(info_or_path, design_id="0") -> str:
    """
    info_or_path: 已解析的 dict 或 info.json 的路径
    design_id: design 的 key（字符串或数字），默认 "0"
    返回 design description（字符串），找不到则抛 KeyError
    """
    if isinstance(info_or_path, (str, Path)):
        info = load_info_json(str(info_or_path))
    else:
        info = info_or_path

    key = str(design_id)
    try:
        return str(info[key]["design description"])
    except KeyError as e:
        raise KeyError(f"Missing key in info.json: {e}")

def main():

    info = load_info_json()
    desc = get_design_description(info, design_name)
    
    #### LLM input ####
    llm_input_query = '''
    You need to generate security-related SVA assertions for a RTL design.
    {$DESIGN_DESCRIPTION}
    The RTL code is provided as follows:
    ```
    {$RTL_CODE}
    ```
    '''
    RTL_PATH = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/src/dut.sv"
    with open(RTL_PATH, 'r', encoding='utf-8') as f:
        rtl_code = f.read()
    query_1 = llm_input_query.replace("{$DESIGN_DESCRIPTION}", desc).replace("{$RTL_CODE}", rtl_code)
    query_list = []
    query_list.append(query_1)

    #### LLM Output result ####
    llm_out_file = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/answer_finial.txt"
    with open(llm_out_file, 'r', encoding='utf-8') as f:
        llm_out_rlt = f.read()
    llm_out_list = []
    llm_out_list.append(llm_out_rlt)

    #### Golden result ####
    golden_file = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/tb/assertion.sva"
    with open(golden_file, 'r', encoding='utf-8') as f:
        golden_rlt = f.read()
    golden_list = []
    golden_list.append(golden_rlt)

    #### retrived context ####
    retrived_file = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/retrived_docs.txt"
    with open(retrived_file, 'r', encoding='utf-8') as f:
        retrived_rlt = f.read()
    retrived_1 = [retrived_rlt]
    retrived_list = []
    retrived_list.append(retrived_1)

    data_dict = {
        'question': query_list,
        'answer': llm_out_list,
        'contexts': retrived_list,
        'ground_truth': golden_list
    }

    dataset = Dataset.from_dict(data_dict)

    end_to_end_results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
    )

    print(end_to_end_results)

if __name__ == '__main__':
    main()

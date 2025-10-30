import os
import openai
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

def main():

    evaluation_samples = []
    #### LLM input ####
    llm_input_query = '''
    * You are now a digital IC security verification engineer proficient in writing SV and SVA, capable of thoroughly analyzing RTL designs, converting test points into verifiable properties and assertions, with a foundational understanding of hardware security.
    * You need to generate security-related SVA assertions based on the provided RTL source files, combined with RTL code.
    RTL design: a register lock module.
    '''
    query_list = []
    query_list.append(llm_input_query)

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
    test_data = {
        "question": ["我们公司的总部在哪里？"],
        "answer": ["我们公司的总部在北京"],
        "contexts": [["根据公司2024年财报显示，我们公司的总部位于中国北京。"]],
        "ground_truth": ["公司的总部在北京"]
    }
    dataset = Dataset.from_dict(test_data)

    end_to_end_results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
    )

    print(end_to_end_results)

if __name__ == '__main__':
    main()

import os
import file_load
import doc_chunk
import vector_store
import prompt_build
import hjson
from langchain_deepseek import ChatDeepSeek

def answer_to_temp(answer, temp_path, filename="1111.txt"):
    os.makedirs(temp_path, exist_ok=True)
    file_path = os.path.join(temp_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(answer)
    print(f"Answer saved to {file_path}")
    return file_path


def property_llm_call(prompt_template, rtl_content, sec_content, example_assertion):
    # build full prompt
    filled_prompt = prompt_template.replace(r'{document}', rtl_content).replace(r'{context}', sec_content).replace(r'{example}', example_assertion)
    # LLM call
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0.4,
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

    design_name = "9"  # 设计名称
    # dir of prompt template
    prompt_path = f"e:/mylife_yanjiu/project/rag_sva/rules/test"
    # load prompt template
    with open(os.path.join(prompt_path, "sva_gen_test_1.md"), "r", encoding="utf-8") as f:
        prompt_template = f.read()

    # dir of src
    src_path = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/src/"
    rtl_files = [src_path + "dut_buggy.sv"]
    with open(rtl_files[0], "r", encoding="utf-8") as f:
        rtl_content = f.read()

    # dir of security requirement
    sec_req_path = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/"
    sec_req_file = sec_req_path + "queries.hjson"
    sec_load = hjson.load(open(sec_req_file, "r", encoding="utf-8"))
    sec_content = sec_load.get("properties", {}).get("DetWVars")
    example_assertion = sec_load.get("examples", {}).get("Ex3")[0]

    # dir of temp files
    temp_path = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/"


    # LLM call for property generation
    answer_property = property_llm_call(prompt_template, rtl_content, sec_content, example_assertion)
    # save answer to temp file
    answer_to_temp(answer_property, temp_path, "answer_property_3.txt")

    return answer_property

if __name__ == "__main__":
    main()

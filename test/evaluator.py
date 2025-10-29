from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_relevancy

design_name = "0"

#### LLM Output result ####
llm_out_file = f"e:/mylife_yanjiu/project/rag_sva/temp/bm_temp/{design_name}/answer_finial.txt"
with open(llm_out_file, 'r', encoding='utf-8') as f:
    llm_out_ret = f.read()

#### Golden result ####
golden_file = f"e:/mylife_yanjiu/project/rag_sva/benchmarks/{design_name}/tb/assertion.sva"
with open(golden_file, 'r', encoding='utf-8') as f:
    golden_ret = f.read()

#### retrived context ####
context_content = ""
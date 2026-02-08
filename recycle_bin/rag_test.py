# main_app.py
import os
########################################################################################
########################################################################################
from trulens.core import TruSession
# from trulens_eval import OpenAI as fOpenAI
import nest_asyncio

os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY")
#设置线程的并发执行
nest_asyncio.apply()
 
#创建评估器对象
tru = TruSession()
#初始化数据库，它用来存储prompt、reponse、中间结果等信息。
tru.reset_database()
 
import numpy as np
from trulens.core import Feedback
from trulens.providers.openai import OpenAI as TruLensOpenAIProvider
from openai import OpenAI as DeepSeekOpenAIClient

deepseek_client = DeepSeekOpenAIClient(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
provider = TruLensOpenAIProvider(client=deepseek_client)

# Define a groundedness feedback function
f_groundedness = (
    Feedback(
        provider.groundedness_measure_with_cot_reasons, name="Groundedness"
    )
    .on_context(collect_list=True)
    .on_output()
)
# Question/answer relevance between overall question and answer.
f_answer_relevance = (
    Feedback(provider.relevance_with_cot_reasons, name="Answer Relevance")
    .on_input()
    .on_output()
)

# Context relevance between question and each context chunk.
f_context_relevance = (
    Feedback(
        provider.context_relevance_with_cot_reasons, name="Context Relevance"
    )
    .on_input()
    .on_context(collect_list=False)
    .aggregate(np.mean)  # choose a different aggregation method if you wish
)

########################################################################################
########################################################################################
from trulens.apps.app import TruApp
from my_llm_app import my_chain

chain_instance = my_chain()
# chain1 = my_chain()

tru_chain = TruApp(
    chain_instance,
    app_name='My_Detailed_RAG_App',
    app_version="base",
    feedbacks=[f_groundedness, f_answer_relevance, f_context_relevance],
)

########################################################################################
########################################################################################

# 运行链，TruLens自动记录和评估
with open(os.path.join("e:/mylife_yanjiu/project/rag_sva/temp/", "query_rag.txt"), "r", encoding="utf-8") as f:
    query_rag = f.read()            # 一般需要注释掉
with open(os.path.join("e:/mylife_yanjiu/project/rag_sva/src/", "aes/spec/aes_spec.md"), "r", encoding="utf-8") as f:
    manually_provided_docs = f.read()
chain_input = {
    "input": query_rag, # 用于检索
    "document": manually_provided_docs # 手动提供的文档
}
# response = tru_chain(chain_input)
# print(response['result'])

with tru_chain as recording:
    result = chain_instance.invoke(chain_input)
    print(result)
tru.get_leaderboard()
from trulens.dashboard import run_dashboard

run_dashboard(tru)

# 启动仪表板查看结果
# tru.run_dashboard()
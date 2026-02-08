import numpy as np
from trulens.core import Feedback
from trulens.providers.openai import OpenAI
from openai import OpenAI as DeepSeekOpenAIClient
from trulens_eval.feedback.provider import openai as TruLensOpenAIProvider
import os

deepseek_client = DeepSeekOpenAIClient(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 请替换为你在 DeepSeek 平台获取的 API Key
    base_url="https://api.deepseek.com"  # DeepSeek API 的端点[6,17,20](@ref)
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
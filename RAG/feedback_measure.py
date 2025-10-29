# feedback_measure.py
import os
from trulens_eval.feedback import Feedback, Groundedness
from openai import OpenAI as DeepSeekOpenAIClient
from trulens_eval.feedback.provider.openai import OpenAI as TruLensOpenAIProvider
from trulens_eval.app import App  # 用于选择上下文
import numpy as np

# 初始化 DeepSeek 提供者
# 关键步骤：创建一个标准的 OpenAI 客户端实例，但将其 base_url 指向 DeepSeek API
deepseek_client = DeepSeekOpenAIClient(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 请替换为你在 DeepSeek 平台获取的 API Key
    base_url="https://api.deepseek.com"  # DeepSeek API 的端点[6,17,20](@ref)
)

openai_provider = TruLensOpenAIProvider(client=deepseek_client)


# 初始化 groundedness 测量类
grounded = Groundedness(groundedness_provider=openai_provider)

def create_rag_triad_feedback(app: App):
    """
    创建用于评估 RAG 三元组（RAG Triad）的反馈函数。
    这是评估 RAG 应用最核心的一组指标。
    Args:
        app (App): 你的 TruLens 应用实例（例如 TruChain 包装后的链），用于选择上下文。
    Returns:
        dict: 包含三个反馈函数的字典。
    """
    # 1. 上下文相关性 (Context Relevance)
    # 衡量检索到的上下文与输入问题的相关程度。
    # 低分表示检索器返回了过多无关信息。
    f_context_relevance = Feedback(openai_provider.context_relevance).on_input().on(
        app.select_context()  # 从应用中选择上下文
    ).aggregate(np.mean)  # 对多个上下文块的平均得分

    # 2. 忠实度/事实基础 (Groundedness)
    # 衡量生成的答案是否严格基于提供的上下文，避免幻觉。
    f_groundedness = Feedback(grounded.groundedness_measure).on(
        app.select_context().collect()  # 收集所有上下文节点
    ).on_output()  # 基于 LLM 的输出
    # 也可使用带推理链的版本，解释更详细但成本更高:
    # f_groundedness = Feedback(grounded.groundedness_measure_with_cot_reasons) ...

    # 3. 答案相关性 (Answer Relevance)
    # 衡量最终答案与原始问题的相关程度。
    f_answer_relevance = Feedback(openai_provider.relevance).on_input_output()

    return {
        "context_relevance": f_context_relevance,
        "groundedness": f_groundedness,
        "answer_relevance": f_answer_relevance
    }

def get_all_feedbacks(app: App = None):
    """
    获取一组常用的反馈函数，便于快速集成到评估中。

    Args:
        app (App, optional): TruLens 应用实例。如果提供，则包含 RAG 三元组反馈。

    Returns:
        list: 一个包含 Feedback 对象的列表，可直接传递给 TruChain 的 `feedbacks` 参数。
    """
    all_feedbacks = []

    # 如果提供了 app 实例，则添加 RAG 三元组反馈
    if app is not None:
        rag_feedbacks = create_rag_triad_feedback(app)
        all_feedbacks.extend(rag_feedbacks.values())

    return all_feedbacks

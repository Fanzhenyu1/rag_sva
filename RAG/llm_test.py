import os
from openevals.llm import create_llm_as_judge
from openevals.prompts import CONCISENESS_PROMPT

# 设置UiUiAPI的端点地址和API密钥
os.environ["OPENAI_BASE_URL"] = "https://sg.uiuiapi.com/v1"  # 替换为UiUiAPI的实际端点
os.environ["OPENAI_API_KEY"] = "sk-Bgpw1h2Zy5zQBYjt8tnhjT5pGhvfzzGPluarZvp6bmrjk7b0"  # 替换为您的UiUiAPI密钥

conciseness_evaluator = create_llm_as_judge(
    prompt=CONCISENESS_PROMPT,
    model="openai:o3-mini",  # UiUiAPI支持此模型
)

inputs = "How is the weather in San Francisco?"
outputs = "Thanks for asking! The current weather in San Francisco is sunny and 90 degrees."

eval_result = conciseness_evaluator(
    inputs=inputs,
    outputs=outputs,
)

print(eval_result)
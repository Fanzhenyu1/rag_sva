
import os
from dotenv import load_dotenv, find_dotenv # 导入 find_dotenv 帮助定位
import openai
from openai import OpenAI
import httpx

# 0. 加载 .env 文件中的环境变量 (增强调试)
print("--- 开始 .env 文件加载调试 ---")
# 尝试在当前工作目录或脚本所在目录查找 .env 文件
# find_dotenv(usecwd=True) 会优先尝试当前工作目录
# find_dotenv() (无参数) 会从脚本位置开始向上查找
dotenv_path_found = find_dotenv(usecwd=True) # 检查当前工作目录
if not dotenv_path_found:
    dotenv_path_found = find_dotenv() # 如果CWD没有，则按标准方式查找（从脚本目录向上）

if dotenv_path_found:
    print(f"DEBUG: 找到 .env 文件路径: {dotenv_path_found}")
    # verbose=True 会打印加载过程的详细信息
    # override=True 表示 .env 文件中的变量会覆盖系统中已存在的同名环境变量
    loaded_successfully = load_dotenv(dotenv_path=dotenv_path_found, verbose=True, override=True)
    if loaded_successfully:
        print("DEBUG: 成功从 .env 文件加载变量。")
    else:
        # 如果 loaded_successfully 为 False，可能表示文件为空或无法解析，
        # 但通常只要文件被找到且非空，python-dotenv 即使内容有问题也可能返回 True，
        # 真正的判断是后续 os.getenv 是否能取到值。
        print("DEBUG: .env 文件已找到，但 load_dotenv() 执行完毕 (请检查 verbose 输出和后续变量值)。")
else:
    print("DEBUG: 未能找到 .env 文件。")
    print("DEBUG: 请确保名为 '.env' 的文件存在于脚本所在目录或项目的根目录中。")

print("--- .env 文件加载调试结束 ---")
print("--- 开始环境变量获取调试 ---")

# 1. 从环境变量加载 API 密钥和基础 URL
api_key = os.getenv("OPENAI_API_KEY")
base_url_from_env = os.getenv("OPENAI_BASE_URL")

# 打印获取到的原始值以供调试
print(f"DEBUG: os.getenv(\"OPENAI_API_KEY\") 返回的值: {'一个字符串 (已隐藏具体内容)' if api_key else 'None'}")
if api_key:
    print(f"DEBUG: API Key 的前5个字符: {api_key[:5]}") # 打印部分以确认

print(f"DEBUG: os.getenv(\"OPENAI_BASE_URL\") 返回的值: {base_url_from_env if base_url_from_env else 'None'}")
print("--- 环境变量获取调试结束 ---")

if not api_key:
    print("--------------------------------------------------------------------")
    print("错误：未能从 .env 文件或环境变量中获取 OPENAI_API_KEY。")
    print("请仔细检查以下几点：")
    print("1. 项目根目录或脚本所在目录中是否存在一个名为 '.env' 的文件。")
    print("   (DEBUG 信息中 '找到 .env 文件路径:' 是否显示了正确的路径？)")
    print("2. '.env' 文件中是否正确定义了 OPENAI_API_KEY='your_actual_key'。")
    print("   (确保键名拼写正确，无多余空格，API密钥值完整无误)。")
    print("3. 确保您的 .env 文件内容与示例格式一致，例如：")
    print("   OPENAI_API_KEY=\"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"")
    print("   OPENAI_BASE_URL=\"https://sg.uiuiapi.com/v1\"")
    print("请查看上面以 'DEBUG:' 开头的详细输出，以帮助定位问题。")
    print("--------------------------------------------------------------------")
    exit() # 必需的 API Key 未找到，退出程序
else:
    print(f"成功加载的 API Key (部分显示): '{api_key[:5]}...{api_key[-4:]}'")

# 基础 URL 可以从环境变量加载，如果未设置，则使用default_base_url = "https://sg.uiuiapi.com/v1"
default_base_url = "OPENAI_BASE_URL" # 您常用的 URL 作为默认值
base_url = base_url_from_env if base_url_from_env else default_base_url
print(f"使用的 Base URL: {base_url}")

if base_url == default_base_url and not base_url_from_env :
    print(f"(提示: OPENAI_BASE_URL 未在 .env 文件或环境变量中指定, 当前使用的是代码中的默认值 '{default_base_url}'。)")

# ... (后续的 OpenAI 客户端初始化、API 调用和错误处理代码保持不变) ...
# 2. 配置 API 客户端
client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    timeout=httpx.Timeout(300.0, connect=60.0),
    max_retries=1,
)

# 3. 准备 API 请求的消息体
messages = [
    {"role": "user", "content": "你好，你好，你能做什么？请用中文回答。"}
]

# 4. 发送请求并处理响应
try:
    print("正在尝试调用 OpenAI API...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4500,
        temperature=0.8,
    )
    if response.choices:
        assistant_reply = response.choices[0].message.content
        print("模型回复:", assistant_reply)
    else:
        print("未能从 API 获取有效回复。")
except openai.AuthenticationError as e:
    print(f"OpenAI API 认证失败: {e}")
    print("这通常意味着 API 密钥无效或没有权限。请再次核对 .env 文件中的 OPENAI_API_KEY 是否为您从 uiuiAPI 获取的正确密钥。")
    print(f"当前尝试使用的 API Key (来自 .env 或环境变量，部分显示): '{api_key[:5]}...{api_key[-4:]}'，Base URL 为: {base_url}")
except openai.APIConnectionError as e:
    print(f"无法连接到 OpenAI API: {e}")
except openai.RateLimitError as e:
    print(f"达到 OpenAI API速率限制: {e}")
except openai.APIStatusError as e:
    print(f"OpenAI API 返回了错误状态码: {e.status_code}")
    print(f"响应详情: {e.response}")
except Exception as e:
    print(f"调用 API 时发生未知错误: {e}")
    print(f"错误类型: {type(e).__name__}")

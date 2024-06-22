#  导入OpenAI的Python SDK
import os
import openai

print(os.getenv("OPENAI_API_KEY"))

# 设置OpenAI API的密钥，该密钥必须在OpenAI的网站上注册并获取
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 创建一个新的对话生成请求，并将响应存储在名为“response”的变量中
response = client.chat.completions.create(
    # 创建一个新的对话生成请求，并将响应存储在名为“response”的变量中
    model="gpt-3.5-turbo",
    # 以列表形式提供对话中的每个消息
    messages=[
        # 第一条消息，表示系统向用户打招呼。
        {"role": "system", "content": "Hello!"},
        # 第一条消息，表示系统向用户打招呼或提问。
        {"role": "user","content": "请告诉我你的脑容量有多大？"},
    ]
)

# 打印对话生成API的响应，其中包括机器生成的回答。
print(response)

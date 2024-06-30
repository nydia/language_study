import os

os.environ["DASHSCOPE_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")

from langchain_community.llms import Tongyi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

def llms_tongyi():    
    llm = Tongyi(temperature=1)
    # 创建一个系统消息，并将它添加到消息列表中
    # 系统消息用于指定模型应该如何理解用户输入
    messages = [
        SystemMessage(content="将以下内容从英文翻译成中文:"),
        HumanMessage(content="what are you?"),
    ]
    # 运行
    result = llm.invoke(messages)
    # 打印结果
    print(result)

def use_chain():
    llm = Tongyi(temperature=1)
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
    res = chain.invoke({"question": question})
    print(res)


llms_tongyi()
use_chain()
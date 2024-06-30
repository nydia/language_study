#!/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Tongyi
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi.middleware.cors import CORSMiddleware

# 使用 Tongyi LLM，并设置温度为 1，代表模型会更加随机，但也会更加不确定
llm = Tongyi(temperature=1)

# 提示模版
system_template = "将以下内容从英文翻译成{language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# 创建一个输出解析器，用于解析模型输出的文本
parser = StrOutputParser()

# 创建应用
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="使用 Langchain 的 Runnable 接口的简单 api 服务器",
)


# 设置所有启用 CORS 的源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# 添加路由
add_routes(
    app,
    prompt_template | llm | parser,
    path="/trans",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
 
llm = OpenAI(model_name="davinci-002",max_tokens=1024)
llm("怎么评价人工智能")
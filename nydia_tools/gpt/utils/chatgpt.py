"""
Chat GPT
"""

import openai
from openai import OpenAI
from utils import gpt

class ChatGpt(gpt.NydiaGpt):
    def __init__(self) -> None:
        pass
    def get_conf(self):
        return super().get_conf()    
    def get_chat(self, my_content):
        client = OpenAI(
          api_key = '',
          organization='',
          project='',
        )

        stream = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": my_content}],
          stream=True,
        )
        for chunk in stream:
          if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
  
chatgpt = ChatGpt()
chatgpt.get_chat("Say this is a test")
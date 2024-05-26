"""
GPT Parent
"""

class NydiaGpt:
    def __init__(self) -> None:
        pass
    def get_conf(self):
        # chatgpt-conf.txt
        file = open("a.txt", "r")
        content = file.readline()
        print(type(content))  # <class 'str'>
        pass
import importlib

def check_module(module_name):
    try:
        importlib.import_module(module_name)
        print(f"模块 '{module_name}' 存在")
    except ImportError:
        print(f"模块 '{module_name}' 不存在")

check_module('requests')
check_module('numpy')
check_module('llama_index')

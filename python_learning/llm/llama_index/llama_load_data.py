from llama_index.core import SimpleDirectoryReader, VectorStoreIndex


def load_data():
    # 读取目录中的文档
    documents = SimpleDirectoryReader("C:/temp/花语大全.txt").load_data()

    # 创建索引
    index = VectorStoreIndex.from_documents(documents)
    
    # 保存索引
    #index.save_to_disk("C:/temp/index.json")
    
def query_data():
    # 加载已保存的索引
    #index = GPTSimpleVectorIndex.load_from_disk("C:/temp/index.json")

    # 提出一个问题
    #response = index.query("Peach Blossom")
    #print(response)
    
     # 读取目录中的文档
    documents = SimpleDirectoryReader(input_dir="C:/temp/llms", recursive=True).load_data()

    # 创建索引
    index = VectorStoreIndex.from_documents(documents)
    
    # set Logging to DEBUG for more detailed outputs
    query_engine = index.as_query_engine()
    
    response = query_engine.query("Peach Blossom")
    print(response)
    
#load_data()
query_data()
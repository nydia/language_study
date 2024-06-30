
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS



def data_loader():
    # 加载
    loader = TextLoader("C:/temp/花语大全.txt")
    loader.encoding = "utf-8"
    documents = loader.load()
    
    # 分割
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    
    # 向量化存储    
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v1", dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
    )
    vectorDB = FAISS.from_documents(docs, embeddings)
    print(vectorDB.index.ntotal)

    # 查询
    query = "Rose"
    query_docs = vectorDB.similarity_search(query)
    print(query_docs[0].page_content)

data_loader()
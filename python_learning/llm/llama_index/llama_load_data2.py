import logging
import sys
import torch
from llama_index.core import PromptTemplate, Settings, SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage, StorageContext, QueryBundle
from llama_index.core.schema import MetadataMode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.node_parser import SentenceSplitter

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

SYSTEM_PROMPT = """You are a helpful AI assistant."""
query_wrapper_prompt = PromptTemplate(
    "[INST]<<SYS>>\n" + SYSTEM_PROMPT + "<</SYS>>\n\n{query_str}[/INST] "
)


llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=2048,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name='C:/files/workspace/python/llm/Qwen1.5-14B-Chat',
    model_name='C:/files/workspace/python/llm/Qwen1.5-14B-Chat',
    device_map="auto",
    model_kwargs={"torch_dtype": torch.float16},
)
Settings.llm = llm

documents = SimpleDirectoryReader("documenC:/temp/花语大全.txtt").load_data()

index = VectorStoreIndex.from_documents(documents, transformations=[SentenceSplitter(chunk_size=256)])

query_engine = index.as_query_engine(similarity_top_k=5)

response = query_engine.query("Peach Blossom")

import os
import shutil
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

KNOWLEDGE_BASE_PATH = "./knowledge_base"
VECTOR_DB_PATH = "./chroma_db_final"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def create_and_persist_db():
    if os.path.exists(VECTOR_DB_PATH):
        shutil.rmtree(VECTOR_DB_PATH)
    loader = DirectoryLoader(KNOWLEDGE_BASE_PATH, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    for doc in documents:
        filename = os.path.basename(doc.metadata['source'])
        topic = filename.replace('_advice.txt', '')
        doc.metadata['topic'] = topic
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vector_db = Chroma.from_documents(texts, embeddings, persist_directory=VECTOR_DB_PATH)
    print("\n--- Vector Database created successfully! ---")

if __name__ == "__main__":
    create_and_persist_db()
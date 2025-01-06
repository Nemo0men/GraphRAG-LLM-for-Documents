# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
# from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai 
from dotenv import load_dotenv
import os
import shutil

# Check and download 'punkt_tab' and 'averaged_perceptron_tagger_eng' if not already available
# try:
#     nltk.data.find('tokenizers/punkt_tab')
# except LookupError:
#     print("Downloading 'punkt_tab' tokenizer...")
#     nltk.download('punkt_tab')
# try:
#     nltk.data.find('tokenizers/averaged_perceptron_tagger_eng')
# except LookupError:
#     print("Downloading 'averaged_perceptron_tagger_eng' tokenizer...")
#     nltk.download('averaged_perceptron_tagger_eng')

# print(os.getenv("OPENAI_API_KEY"))

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv(override=True)
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
openai.api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"
DATA_PATH = "data"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    if not documents or len(documents) == 0:
        raise ValueError("No documents provided for splitting.")
    chunks = split_text(documents)
    save_to_chroma(chunks)




def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()

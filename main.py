import os
import streamlit as st
import pickle
import time
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from openai.error import RateLimitError

# Load .env
load_dotenv(dotenv_path=".env")

# API key check
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY not found in .env file.")
    st.stop()
else:
    st.success("✅ API Key loaded successfully.")

# Title
st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Sidebar for URLs
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()

# Initialize LLM
try:
    llm = OpenAI(temperature=0.9, max_tokens=500, openai_api_key=api_key)
except RateLimitError:
    st.error("⚠️ API rate limit reached. Try again later.")
    st.stop()

if process_url_clicked:
    urls = [u.strip() for u in urls if u.strip()]  # remove empty URLs
    if not urls:
        st.warning("Please enter at least one valid URL.")
    else:
        try:
            loader = UnstructuredURLLoader(urls=urls)
            main_placeholder.text("Data Loading... Started ✅")
            data = loader.load()

            # Split text
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            main_placeholder.text("Splitting text... ✅")
            docs = text_splitter.split_documents(data)

            # Create embeddings
            embeddings = OpenAIEmbeddings(openai_api_key=api_key)
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            main_placeholder.text("Building embeddings... ✅")
            time.sleep(2)

            # Save FAISS index
            with open(file_path, "wb") as f:
                pickle.dump(vectorstore_openai, f)

        except RateLimitError:
            st.error("⚠️ API rate limit reached while processing URLs. Please wait and try again.")

# Question input
query = st.text_input("Ask a question based on the processed articles:")
if query:
    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                vectorstore = pickle.load(f)
                chain = RetrievalQAWithSourcesChain.from_llm(
                    llm=llm, retriever=vectorstore.as_retriever()
                )
                result = chain({"question": query}, return_only_outputs=True)

                st.header("Answer")
                st.write(result["answer"])

                sources = result.get("sources", "")
                if sources:
                    st.subheader("Sources:")
                    for source in sources.split("\n"):
                        st.write(source)

        except RateLimitError:
            st.error("⚠️ API rate limit reached while fetching answer. Please try again later.")


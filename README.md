
FinSight AI: Intelligent Equity Research Assistant

FinSight AI is an AI-powered equity research assistant designed to automate financial news analysis and insight generation.
It leverages LangChain, OpenAI GPT models, and FAISS for intelligent document retrieval and context-aware responses, empowering analysts with instant, research-backed insights.

🚀 Features

News Scraping: Load or upload multiple financial news URLs for content extraction.

AI-Powered Analysis: Process articles using LangChain’s UnstructuredURL Loader and OpenAI embeddings.

Vector Search: Store and query embeddings using FAISS for high-speed semantic search.

Interactive Q&A: Ask financial or market-related questions and receive contextual, source-linked answers.

⚙️ Installation

Clone this repository:

git clone https://github.com/yourusername/finsight-ai.git


Navigate to the project directory:

cd finsight-ai


Install dependencies:

pip install -r requirements.txt


Configure your OpenAI API key in a .env file:

OPENAI_API_KEY=your_api_key_here

🧩 Usage

Launch the Streamlit application:

streamlit run main.py


Input URLs or upload files containing financial articles.

Click “Process Articles” to extract text, create embeddings, and build the FAISS index.

Ask queries related to market trends, company performance, or financial insights — FinSight AI will provide responses with source references.
- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- faiss_store_openai.pkl: A pickle file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.

#  FinSight AI: Intelligent Equity Research Assistant

**FinSight AI** is an AI-powered equity research assistant designed to automate financial news analysis and insight generation.  
It leverages **LangChain**, **OpenAI GPT models**, and **FAISS** for intelligent document retrieval and context-aware responses, empowering analysts with instant, research-backed insights.

---

##  Features

- **News Scraping:** Load or upload multiple financial news URLs for content extraction.  
- **AI-Powered Analysis:** Process articles using LangChain’s UnstructuredURL Loader and OpenAI embeddings.  
- **Vector Search:** Store and query embeddings using FAISS for high-speed semantic search.  
- **Interactive Q&A:** Ask financial or market-related questions and receive contextual, source-linked answers.  

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/finsight-ai.git
2. Navigate to the project directory:
   ```bash
   cd finsight-ai
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Configure your OpenAI API key in a .env file:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   
🧩 Usage
1. Launch the Streamlit application:
streamlit run main.py
2. Input URLs or upload files containing financial articles.
3. Click “Process Articles” to extract text, create embeddings, and build the FAISS index.
4. Ask queries related to market trends, company performance, or financial insights — FinSight AI will provide responses with source references.

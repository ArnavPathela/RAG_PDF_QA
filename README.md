# 📚 Conversational PDF Chatbot

A conversational Retrieval-Augmented Generation (RAG) application that allows users to upload multiple PDF documents and interact with their content through natural language queries.

Built using **Python, Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Groq LLMs**, the application retrieves relevant information from uploaded documents and generates context-aware responses.

## 🚀 Features

- **Multiple PDF Uploads:** Upload and process multiple PDF documents simultaneously.
- **Text Extraction:** Extract textual content from PDFs using PyPDF2.
- **Text Chunking:** Split extracted content into smaller, overlapping chunks for efficient retrieval.
- **Semantic Embeddings:** Generate vector embeddings using Hugging Face's Sentence Transformers.
- **Vector Database:** Store and retrieve document embeddings using FAISS.
- **Conversational Retrieval:** Maintain conversation context to understand follow-up questions.
- **LLM-Powered Responses:** Generate natural language answers using Groq-hosted language models.
- **Interactive Chat Interface:** Chat with your documents through Streamlit.

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation (RAG) pipeline.

```text
             PDF Documents
                   |
                   v
             Text Extraction
                (PyPDF2)
                   |
                   v
              Text Chunking
          (CharacterTextSplitter)
                   |
                   v
           Generate Embeddings
          (Hugging Face Models)
                   |
                   v
             FAISS Vector Store
                   |
                   v
            User Query + History
                   |
                   v
          Conversational Retrieval
               (LangChain)
                   |
                   v
            Relevant Documents
                   |
                   v
              Groq LLM
                   |
                   v
             Generated Answer
                   |
                   v
             Streamlit Chat UI
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| LangChain | RAG pipeline and conversational retrieval |
| FAISS | Vector storage and similarity search |
| Hugging Face | Text embedding generation |
| Sentence Transformers | Semantic embeddings |
| Groq | LLM inference |
| PyPDF2 | PDF text extraction |
| python-dotenv | Environment variable management |

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Obtain an API key from [Groq Console](https://console.groq.com/).

### 5. Run the application

```bash
streamlit run main.py
```

The application will be available at:

```text
http://localhost:8501
```

## 💬 How to Use

1. Launch the application.
2. Upload one or more PDF documents using the sidebar.
3. Click the **Process** button.
4. Wait for the documents to be extracted, chunked, embedded and indexed.
5. Start asking questions about your uploaded documents.
6. Continue the conversation with follow-up questions while retaining conversational context.

## 🧠 Key Concepts Implemented

### Retrieval-Augmented Generation (RAG)

Rather than relying solely on the LLM's pretrained knowledge, the application retrieves relevant document chunks and supplies them as context to the language model.

### Semantic Search

Documents are converted into numerical vector representations using embedding models. FAISS performs similarity searches to identify relevant document chunks based on user queries.

### Conversational Retrieval

Conversation memory allows the application to consider previous interactions when interpreting follow-up questions, making document interaction more natural.

## 🔮 Future Improvements

- [ ] Migrate deprecated LangChain chains to the newer retrieval-chain architecture.
- [ ] Implement persistent conversation history.
- [ ] Add source attribution and page-level citations.
- [ ] Support additional document formats such as DOCX and TXT.
- [ ] Improve retrieval using metadata filtering and reranking.
- [ ] Add document-specific conversation management.
- [ ] Deploy the application to a cloud platform.

## 🔐 Security

- Store API keys in environment variables.
- Keep `.env` and other sensitive configuration files out of version control.
- Add `.env` to `.gitignore`.

## 👨‍💻 Author

**Arnav Pathela**

GitHub: [ArnavPathela](https://github.com/ArnavPathela)

---

*Built as a hands-on project to explore Retrieval-Augmented Generation, vector databases, semantic search, and conversational AI.*

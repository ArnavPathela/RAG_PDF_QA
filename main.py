import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationalRetrievalChain


def get_raw_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text


def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks 


def Store_Vector(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store

def get_conversation_chain(vector):
    llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
    memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
    conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector.as_retriever(),
    memory=memory
    ) 
    return conversation_chain





def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDF's", page_icon=':books:')

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("Chat with Multiple PDF's")
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    user_question =  st.chat_input("Ask your question here")
    if user_question:
        if st.session_state.conversation is None:
            st.warning("Please upload and process your PDFs first.")
        else:
            # Display user message
            with st.chat_message("user"):
                st.markdown(user_question)

            # Get response from LangChain
            response = st.session_state.conversation({
                "question": user_question
            })

            answer = response["answer"]

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(answer)

            # Save messages for Streamlit display
            st.session_state.chat_history.extend([
                {"role": "user", "content": user_question},
                {"role": "assistant", "content": answer}
            ])


    with st.sidebar:
        st.subheader("Your Files")
        pdf_docs = st.file_uploader("Upload your files here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #getting text from pdf 

                raw_text = get_raw_text(pdf_docs)
                #st.write(raw_text)

                #chunking

                chunks = get_chunks(raw_text)
                st.write(chunks)


                #embeddings 
                vector = Store_Vector(chunks)

                st.session_state.conversation = get_conversation_chain(vector)



    




if __name__ == "__main__":
    main()
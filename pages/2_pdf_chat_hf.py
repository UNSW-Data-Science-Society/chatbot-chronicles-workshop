import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import *

# Loop through all the pdfs, loop through all the pages, extract the text and return it as a string
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs: 
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", # split by new line
        chunk_size=1000, # split into chunks of 1000 characters
        chunk_overlap=200, # overlap chunks by 200 characters
        length_function=len 
    )
    chunks = text_splitter.split_text(text) # split the text into chunks
    return chunks

def get_vectorstore(text_chunks, api_key):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorstore

def get_conversation_chain(vectorstore, api_key):
    my_llm = HuggingFaceHub(huggingfacehub_api_token=api_key, repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    # now we need to initialise an instance of memory
    my_memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=my_llm, retriever=vectorstore.as_retriever(),memory=my_memory
    )
    return conversation_chain
    
def handle_user_input(user_question):
    response = st.session_state.conversation.invoke({'question': user_question})
    # st.write(response) # for debugging
    
    # now creating a new session state for our chat history
    st.session_state.chat_history = response['chat_history']
    
    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 ==0:
            st.write(user_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title='Go chat with pdfs', page_icon=':robot_face:')
    
    st.markdown("""
    ## Chat with PDFs :robot_face:

    1. Enter your HuggingFace API key in the input field in the sidebar.
    2. Upload your PDFs and click 'Process.'
    3. Ask any question about your documents in the input box.
    4. Retain your conversation history and ask as many questions as you'd like.
    """)
    
    # add our custom css
    st.write(css, unsafe_allow_html=True)
    
    # checking for and creating session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None 
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    user_question = st.text_input("Go on, get started!")
    
    if user_question:
        handle_user_input(user_question)
        
    st.write(tech_stack_buttons_2, unsafe_allow_html=True)
    
    with st.sidebar:
        HUGGINGFACE_API_KEY = st.text_input("HuggingFace API Key", key="chatbot_api_key", type="password")
        if not HUGGINGFACE_API_KEY:
            st.warning("Please add your HuggingFace API key to continue.")
        
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            if pdf_docs is None or len(pdf_docs) == 0:
                st.warning("Please upload at least one PDF file.")
            else:
                try:
                    with st.spinner("Processing your documents"): 
                        # get the text from the pdfs
                        raw_text = get_pdf_text(pdf_docs)
                        # st.write(raw_text) # run this to test if the text is being extracted correctly
                        
                        # get the text chunks from the pdfs
                        text_chunks = get_text_chunks(raw_text)
                        # st.write(text_chunks)
                        
                        # create vector store
                        vectorstore = get_vectorstore(text_chunks, HUGGINGFACE_API_KEY)
                        
                        # create conversation chain 
                        # we do not want streamlit to re-initialise the conversation chain every time we click any button since it rereuns the code, so we use session state
                        st.session_state.conversation = get_conversation_chain(vectorstore, HUGGINGFACE_API_KEY)
                        
                except Exception as e:
                    st.error(f"An error occurred during document processing: {e}")

# to test app.py 
if __name__ == '__main__':
    main()
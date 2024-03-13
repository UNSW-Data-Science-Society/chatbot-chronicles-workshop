import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to our langchain pdf chat app! 👋")

st.sidebar.success("Navigate through the pages from the menu above.")

st.markdown(
    """
    ## You can ask questions based on your uploaded pdfs
    
    ### Features
    - PDF Processing: The app reads and extracts text content from multiple uploaded PDF documents.
    - Natural Language Interaction: Users can ask questions about the PDFs using natural language input.
    - Conversation History: The app retains conversation history, allowing users to ask multiple questions and maintain context.
    
    ### Tech Stack
    The app is built using the following libraries and APIs:
    - Streamlit: For creating the web interface.
    - LangChain: a framework for developing applications powered by language models.
    - OpenAI's GPT API: To enable natural language interaction with the PDFs. 
        - gpt-3.5-turbo for chat. 
        - text-embedding-ada-002 for embeddings.
    - Hugging Face open source models: 
        - hkunlp/instructor-xl for embeddings.
        - used google/flan-t5-xxl for chat.
    - PyPDF2: For extracting text from PDF documents.
    Other custom libraries for text processing and conversation management.
    
    ### How It Works
    1. PDF Processing: Upon uploading PDFs, the app extracts text from the documents by looping through all the pages of each PDF and combining the text into a single string.

    2. Text Chunking: The extracted text is then split into smaller chunks to facilitate efficient processing and analysis.

    3. Vector Store Creation: The text chunks are used to create a vector store, which involves generating embeddings using OpenAI's GPT model and creating a vector index for efficient similarity matching.

    4. Conversation Chain Initialization: A conversational retrieval chain is established, allowing the app to retain conversation history and provide contextually relevant responses.

    5. User Interaction: Users can ask questions about the uploaded PDFs using natural language input. The app processes the queries, retrieves relevant information from the PDFs, and presents the responses in a conversational format.
"""
)
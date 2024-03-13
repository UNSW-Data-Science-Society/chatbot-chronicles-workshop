# A chatbot for asking questions based on uploaded pdfs

Built using Langchain, APIs from OpenAI and HuggingFace, hosted using streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](insert link here after deployment)

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

### Getting Started

###### To run the webapp locally, follow these steps:
- Clone the repository using ```git clone <repo-name>```
- Install the required libraries by running ```pip install -r requirements.txt```.
- Run the app using ```streamlit run app.py```.

Obtain an OpenAI API key and set it in the app's sidebar.
Upload your PDFs, process them, and start asking questions about the documents.
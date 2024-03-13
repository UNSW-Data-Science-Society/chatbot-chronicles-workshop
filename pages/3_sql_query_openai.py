#importing the necessary libraries
import os
import time
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain.agents import AgentType, create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

#Configuration to connect with the Azure Database
os.environ["SQL_SERVER"]="edu-chatbot-workshop" #Name of the SQL Server
os.environ["SQL_DB"]="chatbot-db"               #Name of the Database  
os.environ["SQL_USERNAME"]="dbmanager1"         #Username   
os.environ["SQL_PWD"]="Meet1504"                #Password


#Creating the connection string

#ODBC stands for open database connectivity which allows us to access the database.
driver = '{ODBC Driver 17 for SQL Server}'

#Creating the connection string
odbc_str = 'mssql+pyodbc:///?odbc_connect=' \
                'Driver='+driver+ \
                ';Server=tcp:' + os.getenv("SQL_SERVER")+'.database.windows.net;' + \
                ';DATABASE=' + os.getenv("SQL_DB") + \
                ';Uid=' + os.getenv("SQL_USERNAME")+ \
                ';Pwd=' + os.getenv("SQL_PWD") + \
                ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

#Intitializing the database
db_engine = create_engine(odbc_str)
db = SQLDatabase(db_engine)



def main():
    logo_url = '/Users/user/Downloads/logo_combined.jpeg' 
    st.set_page_config(page_title = 'Talk with your database')
    st.image(logo_url, width=200)

    st.markdown("""
                ## Talk with your Azure SQL Server Database.
                ### Connect with Azure Cloud SQL server and talk with database on your local device.
 
                1. Enter your OpenAI key in the input field.
                2. Ask any questions about your database.
                """)
    

    #getting the user question
    user_question = st.text_input("Enter any questions about your database.")


    #entering the API key
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        if not openai_api_key:
            st.warning("Please add your OpenAI API key to continue.")
    
    #Intitializing the OpenAI
    llm = ChatOpenAI(openai_api_key=api_key,
                     model="gpt-3.5-turbo", 
                     temperature=0 
                     )
    
    sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    sql_toolkit.get_tools()

    #Initializing the SQL agent
    sqldb_agent = create_sql_agent(
        llm=llm,
        toolkit=sql_toolkit,
        agent_type='openai-tools',
        verbose=True
    )

    if st.button("Submit",type="primary"):
        response = sqldb_agent.invoke({'input': user_question})['output']
        with st.spinner('Processing your query'):
            time.sleep(1)
            st.write(response)
    




if __name__ == '__main__':
    main()
    
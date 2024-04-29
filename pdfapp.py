
import streamlit as st
from PyPDF2 import PdfReader #to read the pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_pdf_info(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000) #breaking the whole text into chunks with overlap
    chunks=text_splitter.split_text(text)
    return chunks

def get_vector(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    text_vector=FAISS.from_texts(text_chunks, embedding=embeddings, allow_dangerous_deserialization=True)
    text_vector.save_local("faiss_index")

def get_conv_chain():
    prompt_template="""
    Answer the questions in details and dont provide answers that are not complete or not aware of 
    Context:\n {context}?\n
    Question:\n {question}?\n

    Answer:

    """
    model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain=load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

##for text box
def user_input(user_question):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001") #defining the embedding
    new_db=FAISS.load_local("faiss_index", embeddings) #loading the saved vector form
    docs=new_db.similarity_search(user_question) #to look for similarity between query and the document

    chain=get_conv_chain()

    response=chain(
        {"input_documents":docs, "question": user_question}, return_only_outputs=True)
    print(response)
    st.write("Reply: ", response["output_text"])


#Streamlit app
def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_info(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector(text_chunks)
                st.success("Done")


if __name__=="__main__":
    main()
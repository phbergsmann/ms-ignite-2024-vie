import gradio as gr

from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader(
    web_paths=("https://pulse.microsoft.com/de-at/microsoft-ignite-austria-session-catalog/",)
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=AzureOpenAIEmbeddings(model="text-embedding-3-small"))

retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

llm = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="gpt-35-turbo",
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def open_ai_prompt(prompt_text):
    return rag_chain.invoke(prompt_text)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

demo = gr.Interface(
    fn=open_ai_prompt, 
    inputs="text", 
    outputs="text",
    allow_flagging=False)
    
demo.launch( server_name="0.0.0.0", server_port=8080 )
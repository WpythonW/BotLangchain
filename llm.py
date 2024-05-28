from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
import streamlit as st
import httpx, os, openai

# Загрузка переменных окружения
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", 
            http_client=httpx.Client(proxies=os.getenv('HTTP_PROXY')),
            openai_api_key=os.getenv('OPENAI_API_KEY'))

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    http_client=httpx.Client(proxies=os.getenv('HTTP_PROXY')),
    openai_api_key=os.getenv('OPENAI_API_KEY'))
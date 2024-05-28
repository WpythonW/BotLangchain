import streamlit as st
from langchain_community.graphs import Neo4jGraph
from dotenv import load_dotenv
load_dotenv()

graph = Neo4jGraph(
    url=os.getenv('NEO4J_URI')
    username=os.getenv('NEO4J_USERNAME')
    password=os.getenv('NEO4J_PASSWORD')
)
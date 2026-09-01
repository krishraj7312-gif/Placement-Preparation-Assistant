from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

def get_llm_chain(retriver):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name='llama3-70b-8192'

    )

    prompt= PromptTemplate(
        input_variables=["context","question"],
        template="""
You are an AI Placement Preparation Assistant.

Use the following context to answer the user's question.

Context:
{context}

Question:
{question}

Instructions:
- Answer based primarily on the provided context.
- If the answer is not available in the context, clearly say that the information is not available in the provided material.
- Keep the answer clear, accurate, and easy to understand.
- For technical questions, explain with a simple example when useful.
- Do not make up information.

Answer:
"""
)
return RetrievalQA.from_chain_type(
    llm=llm,
    chain_type;
)

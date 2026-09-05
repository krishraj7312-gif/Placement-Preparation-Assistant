from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from pathlib import Path
from dotenv import load_dotenv

# Points to server/.env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_llm_chain(retriever):
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an AI Placement Preparation Assistant.

Use the following context to answer the user's question.

Context:
{context}

Question:
{question}

Instructions:
- Answer based primarily on the provided context.
- If the answer is not available in the context, clearly say that the information is not available.
- Keep the answer clear, accurate, and easy to understand.
- For technical questions, explain with a simple example when useful.
- Do not make up information.

Answer:
"""
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
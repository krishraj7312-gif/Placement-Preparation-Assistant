from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exceptions_handlers import catch_exception_middleware

app=FastAPI(title="Placement Assistance API",description="API for placement prep chatbot")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_header=["*"]
)

# middleware exception handlers
app.middlewareeware("http")(catch_exception_middleware)
#router

#1.uploads pdfs docu
#2. asking query

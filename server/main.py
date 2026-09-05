from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exceptions_handlers import catch_exception_middleware
from routes.uploadpdf import router as upload_router
from routes.askquestion import router as ask_router


app = FastAPI(
    title="Placement Preparation Assistant API",
    description="API for AI Placement Preparation Assistant Chatbot",
    version="0.1.0"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)



# middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# routers

# 1. upload pdfs documents
app.include_router(upload_router)
# 2. asking query
app.include_router(ask_router)
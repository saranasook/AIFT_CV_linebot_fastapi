from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.service as service

app = FastAPI(
    title="aiforthai-line-chatbot",
    description="AIFORTHAI LINE CHATBOT WORKSHOP",
    version="1.0.0",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(service.router)


@app.get("/")
def index():
    return "AIFORTHAI LINE CHATBOT WORKSHOP"

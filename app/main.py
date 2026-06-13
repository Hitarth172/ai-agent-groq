from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatMessage(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Agent Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(data: ChatMessage):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": data.message
            }
        ]
    )

    return {
        "response": response.choices[0].message.content
    }
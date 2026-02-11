from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Agent API!"}

@app.get("/ask")
def ask_ai(prompt: str = "Hello, how are you?"):
    response = model.invoke(prompt)
    return {"response": response.content}

import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import re

load_dotenv()
mistral_key = os.getenv("MISTRAL_KEY") 
model = os.getenv("MODEL", "mistral-small-latest")

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()
# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

def run_coding_agent(task: str) -> str:
    if not mistral_key:
        return "Error: MISTRAL_KEY not found in environment variables."
        
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {mistral_key}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": task}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"


# Define your /task endpoint
@app.get("/task")
def handle_task(q: str = Query(...)):
    raw_output = run_coding_agent(q)
    logging.info(f"Task: {q} | Output: {raw_output}")
    status = "error" if raw_output.startswith("Error:") else "success"
    return {
        "status": status,
        "task": q,
        "agent": "mistral-api",
        "output": raw_output,
        "email": "adarsh@gmail.com"
    }
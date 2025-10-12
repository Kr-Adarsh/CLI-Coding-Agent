import os
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import subprocess
import logging
import re

load_dotenv()
COPILOT_PATH = os.getenv("COPILOT_PATH", "copilot")  # fallback to "copilot" if env var missing

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def run_coding_agent(task: str) -> str:
    try:
        result = subprocess.run(
            [COPILOT_PATH, "-p", task],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60
        )
        if result.returncode == 0:
            return (result.stdout or "").strip()
        else:
            return f"Error: {(result.stderr or '').strip()}"
    except Exception as e:
        return f"Exception: {e}"


# Define your /task endpoint
@app.get("/task")
def handle_task(q: str = Query(...)):
    raw_output = run_coding_agent(q)
    logging.info(f"Task: {q} | Output: {raw_output}")
    return {
        "task": q,
        "agent": "copilot-cli",
        "output": raw_output,
        "email": "23f2000927@ds.study.iitm.ac.in"
    }
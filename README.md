# CLI-Coding-Agent

## Overview

CLI-Coding-Agent is a locally hosted coding assistant that joins a FastAPI backend with GitHub Copilot CLI. Users interact through a web interface to submit programming tasks or factual queries. The backend invokes Copilot directly from the command line, returning generated code or answers in real time—no external cloud dependency.

You can access the [Site from here](https://kr-adarsh.github.io/CLI-Coding-Agent/)
<h2>Working demo</h2> <a href="https://www.youtube.com/watch?v=4k6MRNkUiKU" rel="noopener noreferrer"> <img src="https://img.youtube.com/vi/4k6MRNkUiKU/maxresdefault.jpg" alt="CLI-Coding-Agent Demo" style="max-width:100%; height:auto;"> </a>

## Features

- Clean web interface for submitting coding tasks or general questions
- Real-time code generation and response via Copilot CLI
- Handles programming problems, factual queries, fun facts, and more
- Designed for local development and experimentation
- Modern, responsive design, easily customizable theme
- Robust error handling and logging


## Setup

1. **Install GitHub Copilot CLI**
Follow official instructions for [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli) and authenticate locally.
2. **Clone the project**

```sh
git clone https://your-repo-url/cli-coding-agent.git
cd cli-coding-agent
```

3. **Install Python dependencies**

```sh
pip install fastapi uvicorn python-dotenv
```

4. **Configure Copilot CLI path**
Create a `.env` file in your project folder:

```
COPILOT_PATH=C:\Users\yourname\AppData\Roaming\npm\copilot.cmd
```

5. **Run the FastAPI server**

```sh
uvicorn main:app --reload
```

6. **Open the frontend**
Open `frontend-interface.html` in your browser.

## Working Model

1. The web page provides an input box for coding tasks or factual requests.
2. On submit, the frontend sends the user’s query to the FastAPI backend.
3. The backend invokes Copilot CLI with the submitted task via a subprocess.
4. Copilot CLI generates a code solution, executes it, or answers the query.
5. The backend captures Copilot’s output.
6. The result is presented in the browser, formatted for readability.

This workflow allows users to generate solutions and answers on their local machine interactively and instantly.

## Customization

- Edit `frontend-interface.html` to change color scheme, add tips, or tweak layout.
- Refine backend logging or error handling as needed.

## Contributing

Feedback and improvements are welcome. Issues and pull requests encouraged.

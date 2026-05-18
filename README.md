# CLI-Coding-Agent

## Overview

CLI-Coding-Agent is a powerful coding assistant that pairs a FastAPI backend with the Mistral API. Users interact through a beautifully designed web interface to submit programming tasks, architecture queries, or factual questions. The backend directly communicates with Mistral's advanced LLMs (like `mistral-small-latest`), returning generated code or answers in real-time.

You can access the [Site from here](https://kr-adarsh.github.io/CLI-Coding-Agent/) - \[*Note:* The backend server is currently hosted on Hugging Face Spaces to keep the site active.\]

<h2>Working demo</h2> <a href="https://www.youtube.com/watch?v=4k6MRNkUiKU" rel="noopener noreferrer"> <img src="https://img.youtube.com/vi/4k6MRNkUiKU/maxresdefault.jpg" alt="CLI-Coding-Agent Demo" style="max-width:100%; height:auto;"> </a>
*(Demo reflects the legacy Copilot CLI version, the new Mistral API backend is even faster!)*

## Features

- **Premium Web Interface**: A beautifully crafted, modern UI with gradients, glassmorphism, and responsive design.
- **Mistral API Powered**: Generates code, explains architecture, and answers queries using state-of-the-art Mistral models.
- **Advanced Code Formatting**: Features custom `marked.js` and `highlight.js` integration for perfect markdown rendering.
- **Smart Syntax Highlighting**: Code blocks are perfectly styled with a dark theme, language tags, and one-click "Copy" buttons.
- **Robust Backend**: Built on FastAPI with asynchronous capabilities, logging, and smart error handling.


## Setup

1. **Clone the project**

```sh
git clone https://your-repo-url/cli-coding-agent.git
cd cli-coding-agent
```

2. **Install Python dependencies**

```sh
pip install fastapi uvicorn python-dotenv requests
```

3. **Configure Environment Variables**
Create a `.env` file in your project folder to store your Mistral API key and specify your model choice:

```
MISTRAL_KEY=your_mistral_api_key_here
MODEL=mistral-small-latest
```

4. **Run the FastAPI server**

```sh
uvicorn main:app --reload
```

5. **Open the frontend**
Open `index.html` in your browser.


## Working Model

1. The web page provides a clean input box for coding tasks or factual requests.
2. On submit, the frontend sends the user’s query to the FastAPI backend.
3. The backend formulates a prompt and calls the Mistral API using Python's `requests` library.
4. The backend captures Mistral’s markdown output and streams it to the frontend.
5. The frontend custom parser processes the markdown, applies syntax highlighting to any code blocks, injects copy buttons, and renders it beautifully.

## Customization

- Edit `index.html` to tweak the UI, change the CSS styling, or modify the markdown renderer options.
- Change the `MODEL` in your `.env` to switch between `mistral-tiny`, `mistral-small`, or `mistral-large` depending on your needs.

## Contributing

Feedback and improvements are welcome. Issues and pull requests encouraged.

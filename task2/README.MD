# 🤖 Local Multimodal AI Assistant using Ollama

## Overview

This project implements a local AI assistant using Ollama and open-source AI models. The application provides conversational AI, PDF document question answering, and image analysis through a clean Streamlit web interface.

All AI processing runs locally on the user's machine, ensuring privacy and eliminating the need for external APIs.

---

## Features

### 💬 Chatbot

- General-purpose conversational chatbot powered by Llama 3
- Maintains conversation history during the active session
- Answers general knowledge and programming questions
- Interactive chat interface using Streamlit

### 📄 PDF Question Answering

- Upload PDF documents
- Extract text using PyPDF
- Ask questions about uploaded documents
- Generate summaries and document insights

### 🖼️ Image Analysis

- Upload image files
- Analyze images using Moondream
- Ask questions about image contents
- Perform multimodal image understanding

### ⚙️ Additional Features

- Error handling for invalid inputs
- Streamlit web interface
- Local AI inference using Ollama
- Session-based conversation memory
- Loading indicators for model responses

---

## Technologies Used

- Python
- Ollama
- Llama 3
- Moondream
- Streamlit
- PyPDF
- Pillow

---

## System Architecture

```text
                User
                  │
        ┌─────────┴─────────┐
        │                   │
     PDF/Text           Image
        │                   │
        ▼                   ▼
     Llama 3           Moondream
        │                   │
        └─────────┬─────────┘
                  ▼
              Response
```

---

## Installation

### 1. Install Ollama

Download and install Ollama from:

https://ollama.com

### 2. Download Required Models

```bash
ollama pull llama3
ollama pull moondream
```

### 3. Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 4. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application:

```bash
python -m streamlit run app.py
```

or

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

---

## Project Structure

```text
project/
│
├── README.md
├── requirements.txt
│
├── app.py
│
├── modle_1.py
│
└── screenshots/
    ├── chatbot.png
    ├── pdf_qa.png
    └── image_analysis.png
```

---

## Models Used

### Llama 3

Used for:

- General chatbot
- PDF question answering
- Document summarization

### Moondream

Used for:

- Image analysis
- Visual question answering
- Multimodal understanding

---

## Example Use Cases

### Chatbot

```text
What is machine learning?
Explain neural networks.
Write a Python function for binary search.
```

### PDF Question Answering

```text
Summarize this document.
What skills are listed in this resume?
What are the main findings of the report?
```

### Image Analysis

```text
Describe this image.
How many people are visible?
What objects can you identify?
```

---

## Future Improvements

- Support for additional document formats
- Multiple document uploads
- Model selection interface
- Chat history export
- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Audio input and transcription

---

## Learning Outcomes

This project demonstrates:

- Local LLM deployment
- Multimodal AI applications
- Streamlit application development
- PDF text extraction
- Image processing workflows
- Session state management
- Error handling
- Ollama integration

---

## Screenshots

### Chatbot

![Chatbot](screenshots/chat_bot.png)

### PDF Question Answering

![PDF QA](screenshots/pdf_qa.png)

### Image Analysis

![Image Analysis](screenshots/image_qa.png)



## Author

Krish Singh
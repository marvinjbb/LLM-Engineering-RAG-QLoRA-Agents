# LLM Engineering Fundaments

Building practical Large Language Model (LLM) applications from first principles using Python, OpenAI APIs, local models with Ollama, prompt engineering, tokenization, web scraping, and multi-step AI workflows.

---

## Overview

This repository contains projects and exercises focused on understanding how Large Language Models work from an engineering perspective.

The goal is to move beyond simply using AI tools and learn how to design, build, and deploy real-world AI applications.

Topics covered include:

* Tokenization
* Prompt Engineering
* OpenAI API Integration
* LLM Message Architecture
* Context Windows
* Stateless LLM Design
* Local LLMs with Ollama
* Website Scraping
* AI-Powered Summarization
* Multi-Step AI Workflows
* Structured Outputs
* Streaming Responses

---

# What I Learned

## 1. Tokenization

Large Language Models do not process text directly.

They process tokens.

Using the `tiktoken` library, I explored:

* Encoding text into tokens
* Decoding tokens back into text
* Understanding token IDs
* Estimating API costs
* Understanding context window limitations

Example:

```python
tokens = encoding.encode(
    "Hi my name is Ed and I like banoffee pie"
)
```

This demonstrated how language is converted into numerical representations before being processed by an LLM.

---

## 2. LLM APIs

Learned how to interact with Large Language Models using the OpenAI Python SDK.

### Client Initialization

```python
from openai import OpenAI

client = OpenAI()
```

### Sending Messages

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"}
]
```

### Generating Responses

```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
```

This introduced the core architecture used by modern AI applications.

---

## 3. Understanding the Illusion of Memory

One of the most important lessons was understanding that LLMs are completely stateless.

The model does not remember previous conversations.

Instead:

1. Every request is independent.
2. The application sends the conversation history.
3. The model receives the history as context.
4. The model predicts the next tokens.

This creates the illusion of memory.

Understanding this concept is fundamental when building:

* Chatbots
* AI Assistants
* RAG Systems
* Agentic Workflows
* Multi-Agent Systems

---

## 4. Website Scraping

Built a website scraper using:

* Requests
* BeautifulSoup

Features:

* Extract page titles
* Extract website content
* Remove irrelevant elements
* Extract links
* Prepare content for LLM processing

Example:

```python
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
```

This forms the foundation of many AI systems that consume external information.

---

## 5. AI Website Summarizer

Built a website summarization application using:

* BeautifulSoup
* Requests
* Ollama
* Llama 3.2

Workflow:

```text
Website
   ↓
Scraper
   ↓
Extract Content
   ↓
Prompt Construction
   ↓
Local LLM (Llama 3.2)
   ↓
Summary
```

The application:

* Fetches website content
* Cleans irrelevant text
* Sends content to a local LLM
* Generates concise summaries

This project introduced practical prompt engineering and local inference.

---

## 6. Prompt Engineering

Learned how system prompts influence model behavior.

Example:

```python
system_prompt = """
You are a snarky assistant that analyzes websites
and creates humorous summaries.
"""
```

By changing only the prompt, the same model can behave differently.

Examples:

* Professional
* Technical
* Friendly
* Humorous
* Educational

This demonstrated how prompts function as lightweight behavior control mechanisms.

---

## 7. Local LLM Deployment with Ollama

Built applications using locally hosted models.

### Stack

* Ollama
* Llama 3.2
* OpenAI-Compatible API

Configuration:

```python
ollama = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

Benefits:

* No API costs
* Offline execution
* Faster experimentation
* Greater privacy

This introduced the concept of self-hosted AI systems.

---

## 8. Multi-Step AI Workflows

Built a company brochure generator that combines multiple LLM calls into a single workflow.

### Workflow

```text
Company Website
        ↓
Link Extraction
        ↓
Link Selection by LLM
        ↓
Content Collection
        ↓
Brochure Generation
        ↓
Markdown Output
```

The application:

1. Scrapes a company website
2. Extracts all links
3. Uses an LLM to identify relevant pages
4. Collects additional content
5. Generates a professional company brochure

This was my first introduction to Agentic AI design patterns.

---

## 9. Structured Outputs

Learned how LLMs can generate structured JSON responses.

Example:

```json
{
  "links": [
    {
      "type": "about page",
      "url": "https://company.com/about"
    }
  ]
}
```

This technique is critical for:

* AI Agents
* Tool Calling
* Workflow Automation
* Production AI Systems

---

## 10. Streaming Responses

Implemented token streaming to create real-time user experiences.

```python
stream=True
```

Benefits:

* Faster perceived response times
* Improved user experience
* ChatGPT-style interfaces

This is commonly used in production AI applications.

---

# Technologies Used

* Python
* OpenAI SDK
* Ollama
* Llama 3.2
* GPT Models
* BeautifulSoup4
* Requests
* Tiktoken
* JSON
* Markdown
* Jupyter Notebooks

---

# Projects

## Project 1 — Website Summarizer

Summarizes website content using a local LLM.

### Skills Demonstrated

* Web Scraping
* Prompt Engineering
* Local LLM Inference
* API Integration

---

## Project 2 — AI Company Brochure Generator

Generates professional company brochures from public websites.

### Skills Demonstrated

* Multi-Step Prompting
* Structured Outputs
* Web Scraping
* Agentic Workflows
* Content Generation

---

# Key Engineering Takeaways

The most important lessons from these projects were:

* LLMs are token prediction engines.
* Every LLM call is stateless.
* Context creates the illusion of memory.
* Prompt engineering is software engineering.
* AI applications are workflows, not just model calls.
* Local models are practical for development and experimentation.
* Structured outputs are essential for automation.
* Multi-step workflows are the foundation of AI agents.

---

# Future Topics

Upcoming areas of study include:

* Advanced Prompt Engineering
* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)
* Tool Calling
* AI Agents
* Multi-Agent Systems
* AI Evaluation
* Production AI Architecture
* AI Infrastructure

---

# Author

## Marvin Joseph

AI Engineer in Training focused on building production-grade AI systems for:

* Financial AI
* Research Agents
* RAG Systems
* AI Automation
* Intelligent Workflows

### Connect With Me

* LinkedIn: [www.linkedin.com/in/marvin-joseph-bogere](http://www.linkedin.com/in/marvin-joseph-bogere)
* GitHub: github.com/marvinjbb

---

> Learn it. Build it. Deploy it. Improve it.

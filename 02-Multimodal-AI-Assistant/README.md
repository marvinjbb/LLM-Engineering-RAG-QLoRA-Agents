# Multimodal AI Assistant

A Python-based AI application project that develops a conversational assistant from model API integration through to tool use, database retrieval, image generation, and text-to-speech.

The final prototype, **FlightAI**, is a multimodal airline support assistant that can answer customer questions, retrieve ticket prices from a local database, generate destination imagery, and create spoken responses.

---

## Overview

This project explores the practical building blocks behind modern AI applications:

- Connecting to frontier models through APIs
- Working with OpenAI-compatible model providers
- Building interactive interfaces with Gradio
- Managing conversation history for chat applications
- Using LLM tool calling to retrieve structured data
- Connecting an assistant to a SQLite database
- Generating images and speech as part of an AI workflow
- Comparing model capabilities through SVG generation experiments

The project is organized as a sequence of focused implementations, with each notebook building on a distinct capability.

---

## Core Capabilities

### Multi-Provider LLM Integration

Connects to multiple model providers using native SDKs and OpenAI-compatible endpoints. The implementation explores model selection, reasoning settings, routing layers, prompt caching, and local model access.

### Gradio Interfaces

Builds browser-based interfaces for LLM applications using Gradio. Includes text interfaces, authentication examples, interface customization, and a company brochure generator.

### Conversation-Aware Chatbot

Implements a chatbot that sends the current user message together with prior conversation history, allowing the model to respond with context from the conversation.

### Tool-Calling Assistant

Builds an airline support assistant that can identify when it needs external information, request a tool call, retrieve ticket prices, and use the result in its final response.

### Database-Backed Retrieval

Uses SQLite as a local structured data source for airline ticket prices. This keeps price retrieval deterministic instead of relying on the model to invent answers.

### Multimodal Responses

Extends the assistant with:

- AI-generated destination images
- Text-to-speech audio responses
- Database-backed ticket pricing
- Tool-calling workflows
- Chat-based customer support

### SVG Model Comparison

Tests multiple LLMs on structured SVG generation and renders the results for visual comparison.

---

## Architecture

```text
User
  ↓
Gradio Interface
  ↓
Chat Controller
  ↓
LLM API
  ├── Conversation History
  ├── Tool Definitions
  ├── SQLite Ticket Database
  ├── Image Generation
  └── Text-to-Speech Generation
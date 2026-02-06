# 🧠 Kimi Structured OCR API

**Repository:** `ashgov07/kimi-structured-ocr`  
**Author:** Ashwanth  
**Version:** 1.0.0  
**Tech Stack:** FastAPI · Ollama · Vision LLM · Python  

A lightweight, production-ready **image-to-structured-JSON OCR service** powered by a local / cloud LLM via **Ollama**.  
Designed for **medical, technical, and semi-structured images** where clean JSON output is critical.

---

## ✨ Key Features

- 📷 **Image OCR via Vision LLM**
- 🧾 **Structured JSON extraction** (auto-cleaned)
- 🚀 **FastAPI-based REST API**
- 🧠 Powered by **Ollama LLMs** (e.g. `kimi-k2.5`, `gemma3`)
- 🧼 Automatic **JSON cleanup from LLM responses**
- 🔌 Plug-and-play for downstream pipelines (RAG, DB, analytics)

---

## 📂 Repository Structure

```text
ashgov07-kimi-structured-ocr/
└── main.py        # FastAPI OCR service

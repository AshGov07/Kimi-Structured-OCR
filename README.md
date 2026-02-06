# 🧠 Kimi Structured OCR

**Author:** Ashwanth  
**Version:** 1.1.0  
**Stack:** FastAPI · Ollama · Vision LLM · Python · HTML/CSS  

A modern **Image → Structured JSON OCR system** powered by **Vision LLMs via Ollama**, featuring a **glassmorphism-based web UI** and a clean REST API.

Built for **medical images, reports, tables, boxed text, and semi-structured documents** where precision and copy-ready JSON output matter.

---

## ✨ What This Project Does

- Accepts **image uploads** (medical scans, documents, reports)
- Sends images to a **Vision-capable LLM** via Ollama
- Forces **structured JSON extraction**
- Automatically **cleans and validates LLM output**
- Provides:
  - 🚀 REST API (`/ocr`)
  - 🎨 Web UI (`/docs/ui`)

---

## 🧩 Key Features

- 📷 Vision-based OCR (no traditional OCR engines)
- 🧾 Copy-ready **structured JSON output**
- 🧼 Automatic JSON extraction from verbose LLM responses
- 🧠 Model-agnostic (Gemma, Kimi, Llava, Qwen-VL, etc.)
- 🌐 Interactive **glassmorphism UI**
- 🔌 Drop-in microservice for AI pipelines

---

## 📂 Repository Structure

```text
ashgov07-kimi-structured-ocr/
├── README.md        # Documentation
├── main.py          # FastAPI backend (OCR + UI serving)
└── ui.html          # Glassmorphism web interface
```

---

## 🏗️ System Architecture

```text
Browser UI / API Client
          ↓
     FastAPI Server
          ↓
     Image → Base64
          ↓
   Ollama Vision LLM
          ↓
   LLM Text Response
          ↓
 JSON Detection & Cleanup
          ↓
   Structured JSON Output
```

---

## 🧠 Model Configuration

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "kimi-k2.5:cloud"
```

Supported models include:
- `gemma3:12b`
- `llava`
- `qwen-vl`
- Any Ollama-compatible vision model

---

## 🚀 API Endpoints

### POST /ocr

Upload an image and receive structured OCR output.

**Request**
- `multipart/form-data`
- Field: `file` (image only)

**Example**
```bash
curl -X POST http://localhost:8000/ocr \
  -F "file=@sample.png"
```

**Successful Response**
```json
{
  "patient_name": "John Doe",
  "age": 45,
  "finding": "Benign cyst",
  "measurement": "2.3 cm"
}
```

**Fallback Response**
```json
{
  "text": "raw LLM output",
  "note": "Could not parse JSON automatically."
}
```

---

### GET /docs/ui

Launch the interactive web UI.

```
http://localhost:8000/docs/ui
```

Features:
- Image preview
- Drag & drop upload
- Loading indicators
- Copy-ready JSON output
- Glassmorphism design

---

## 🎨 Web UI

- Liquid-glass card layout
- Background image served via FastAPI
- Zero frontend frameworks
- Fully self-contained (`ui.html`)

---

## 🧼 JSON Cleaning Strategy

1. Detects JSON inside Markdown blocks  
2. Falls back to raw `{ ... }` detection  
3. Attempts strict JSON parsing  
4. Returns raw text only if parsing fails  

Designed to be resilient to LLM verbosity.

---

## ⚙️ Running the Project

### Install dependencies
```bash
pip install fastapi uvicorn pillow requests
```

### Start Ollama
```bash
ollama serve
```

Pull your model:
```bash
ollama pull kimi-k2.5
```

---

### Run the server
```bash
uvicorn main:app --reload
```

- API: http://localhost:8000  
- UI: http://localhost:8000/docs/ui  
- Swagger: http://localhost:8000/docs  

---

## 🔐 Validation & Safety

- Accepts only image files
- Graceful error handling
- Timeout-protected LLM calls

---

## 🎯 Ideal Use Cases

- Medical OCR (ultrasound, reports, scans)
- Table and boxed-text extraction
- OCR → RAG pipelines
- OCR → database ingestion
- AI-assisted document understanding

---

## 🛠️ Customization

Modify behavior via:
```python
FIXED_OCR_PROMPT
MODEL_NAME
```

---

## 🗺️ Roadmap

- [ ] JSON schema enforcement
- [ ] Batch image uploads
- [ ] Docker deployment
- [ ] Authentication & rate limiting
- [ ] Streaming OCR responses

---

## 📄 License

MIT License.

---

## ⭐ Final Note

This repository is built as a **core OCR microservice**, not a demo.

If you're building **vision-based AI pipelines or medical OCR systems**, this is a strong, extensible foundation.

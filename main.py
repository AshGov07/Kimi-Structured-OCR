# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import requests

# OLLAMA_BASE_URL = "http://localhost:11434"

# app = FastAPI(
#     title="Local LLM Service",
#     version="1.0.0",
#     description="FastAPI wrapper over Ollama"
# )

# # ---------- Request / Response Schemas ----------

# class GenerateRequest(BaseModel):
#     prompt: str
#     model: str = "gemma3:12b"
#     stream: bool = False

# class GenerateResponse(BaseModel):
#     response: str

# # ---------- Endpoints ----------

# @app.post("/generate", response_model=GenerateResponse)
# def generate_text(req: GenerateRequest):
#     try:
#         r = requests.post(
#             f"{OLLAMA_BASE_URL}/api/generate",
#             json={
#                 "model": req.model,
#                 "prompt": req.prompt,
#                 "stream": req.stream
#             },
#             timeout=120
#         )
#         r.raise_for_status()
#         data = r.json()
#         return {"response": data["response"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))






import json
import re
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
import requests
import base64
from PIL import Image
import io
import os

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "kimi-k2.5:cloud"

FIXED_OCR_PROMPT = "extract the details properly and place it in json format. I must be able to copy it.I want the thinking and output displayed quickly. No bluffing"


# FIXED_OCR_PROMPT = """ACT AS A PRECISE MEDICAL OCR ENGINE.\n
#     Extract the patient result.\n
#     DO NOT provide any introductory or concluding remarks."""

app = FastAPI(
    title="Image OCR API",
    version="1.0.0",
    description="FastAPI OCR service powered by Ollama + Gemma3"
)

def image_to_base64(image_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@app.get("/docs/ui", response_class=HTMLResponse)
async def serve_ui():
    file_path = os.path.join(os.path.dirname(__file__), "ui.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/background.png")
async def background_image():
    file_path = os.path.join(os.path.dirname(__file__), "Optical-Character-Recognition-.png")
    return FileResponse(file_path)

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    try:
        image_bytes = await file.read()
        image_base64 = image_to_base64(image_bytes)

        payload = {
            "model": MODEL_NAME,
            "prompt": FIXED_OCR_PROMPT,
            "images": [image_base64],
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload, timeout=180)
        r.raise_for_status()

        result = r.json()
        valid_response = result.get("response", "").strip()

        # Attempt to extract JSON from Markdown code blocks
        json_match = re.search(r"```json\s*(\{.*?\})\s*```", valid_response, re.DOTALL)
        
        # If no markdown block, look for the first '{' and last '}' to try matching a raw JSON object
        if not json_match:
            json_match = re.search(r"(\{.*\})", valid_response, re.DOTALL)

        if json_match:
            try:
                # Parse the extracted string as JSON
                cleaned_data = json.loads(json_match.group(1))
                return JSONResponse(content=cleaned_data)
            except json.JSONDecodeError:
                # If parsing fails, fall back to returning raw text
                pass

        # Fallback: Return raw text if no JSON structure found or parsing failed
        return JSONResponse(
            content={
                "text": valid_response,
                "note": "Could not parse JSON automatically."
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

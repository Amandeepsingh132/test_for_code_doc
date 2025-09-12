from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from translator import Translator
from saver import save_translation

app = FastAPI(title="Gemini Translator API")

translator = Translator()

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class SaveRequest(BaseModel):
    text: str
    filename: str


@app.post("/translate")
async def translate(req: TranslationRequest):
    try:
        translated = translator.translate(req.text, req.target_language)
        return {"original": req.text, "translated": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/save")
async def save(req: SaveRequest):
    try:
        save_translation(req.text, req.filename)
        return {"status": "success", "file": req.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

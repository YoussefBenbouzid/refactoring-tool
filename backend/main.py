from fastapi import FastAPI
from pydantic import BaseModel
import servizi.generazione_prompt as gnp
import servizi.comunicazione_llm as cmn

app = FastAPI() # Istanziazione applicazione FastAPI

class CodiceRequest(BaseModel):
    codice: str

class UrlRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/processo_snippet")
async def processo_snippet(request: CodiceRequest):
    codice = request.codice
    prompt = gnp.generazione_prompt_snippet(codice)
    risposta = cmn.comunicazione_gpt(prompt)
    return {"risposta": risposta}

@app.post("/processo_repository")
async def processo_repository(request: UrlRequest):
    url = request.url
    return {"risposta": risposta}
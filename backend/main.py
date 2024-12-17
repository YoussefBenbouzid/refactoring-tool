from fastapi import FastAPI
from pydantic import BaseModel
import servizi.generazione_prompt as gnp
import servizi.comunicazione_llm as cmn

app = FastAPI() # Istanziazione applicazione FastAPI

class CodiceRequest(BaseModel):
    codice: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/genera_risposta")
async def genera_risposta(request: CodiceRequest):
    codice = request.codice
    prompt = gnp.generazione_prompt(codice)
    risposta = cmn.comunicazione_gpt(prompt)
    return {"risposta": risposta}
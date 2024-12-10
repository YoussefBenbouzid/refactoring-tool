from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import servizi.generazione_prompt as gnp
import servizi.comunicazione_llm as cmn

app = FastAPI() # Istanziazione applicazione FastAPI

class CodiceRequest(BaseModel):
    codice: str

@app.post("/genera")
async def genera_risposta(request: CodiceRequest):
    codice = request.codice
    prompt = gnp.genera_prompt(codice)
    output = cmn.comunicazione_gpt(prompt)
    return {"output": output}

uvicorn.run(app, host="0.0.0.0", port=8000)
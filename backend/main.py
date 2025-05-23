from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from servizi import interventi_file as inf
from servizi import valutazione as vlt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DatiUrl(BaseModel):
    owner: str
    repo: str

@app.post("/repository")
async def analizza_repository(dati: DatiUrl):
    url_repository = f"https://api.github.com/repos/{dati.owner}/{dati.repo}/contents/"
    inf.estrai_codici_da_repository(url_repository)

#@app.post("/snippet")
    # Implementare
    # Implementare
    # Implementare
    # Implementare

#@app.post("/allegati")
    # Implementare
    # Implementare
    # Implementare
    # Implementare

@app.post("/valuta")
async def valuta():
    vlt.valutazione()

@app.post("/reset")
async def reset():
    inf.svuota_cartelle()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
import servizi.generazione_prompt as gnp
import servizi.comunicazione_llm as cmn
import servizi.interventi_file as inf

app = FastAPI()

#class DatiRepository(BaseModel): # da ripristinare una volta sistemato front end
    #owner: str # da ripristinare una volta sistemato front end
    #repo: str # da ripristinare una volta sistemato front end

#class CodiceRequest(BaseModel):
    #codice: str

############ Da passare con front end ############
owner = "YoussefBenbouzid"
repo = "refactoring-tool"
##################################################

@app.post("/repository")
#async def analizza_repository(data: DatiRepository): # da ripristinare una volta sistemato front end
    #url_repsotory = f"https://api.github.com/repos/{data.owner}/{data.repo}/contents/" # da ripristinare una volta sistemato front end
async def analizza_repository(): # da rimuovere una volta sistemato front end
    url_repository = f"https://api.github.com/repos/{owner}/{repo}/contents/" # da rimuovere una volta sistemato front end
    inf.estrai_file_da_repository(url_repository)

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
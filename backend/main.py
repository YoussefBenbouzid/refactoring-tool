from fastapi import FastAPI
from pydantic import BaseModel
import servizi.generazione_prompt as gnp
import servizi.comunicazione_llm as cmn
import servizi.interventi_repository as irp

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
    #url = f"https://api.github.com/repos/{data.owner}/{data.repo}/contents/" # da ripristinare una volta sistemato front end
async def analizza_repository(): # da rimuovere una volta sistemato front end
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/" # da rimuovere una volta sistemato front end
    irp.estrai_file_da_repository(url)


#@app.post("/snippet")
#async def analizza_snippet(request: CodiceRequest):
    #codice = request.codice
    #prompt = gnp.prompt_analisi(codice)
    #risposta = cmn.comunicazione_gpt4(prompt)
    #return {"risposta": risposta}
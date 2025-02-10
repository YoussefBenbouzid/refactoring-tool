import os
import requests
import base64
from servizi import generazione_prompt as gnp
from servizi import comunicazione_llm as cmn

# Funzione che crea un file nella cartella di destinazione contenente codice rifattorizzato dall'LLM
def crea_file_in_cartella(codice_rifattorizzato, nome_file, cartella):
    percorso_cartella = os.path.join(os.path.dirname(os.path.abspath(__file__)), cartella)
    percorso_file = os.path.join(percorso_cartella, nome_file)
    with open(percorso_file, 'w', encoding='utf-8') as file:
        file.write(codice_rifattorizzato)

# Funzione che analizza e rifattorizza codice con i tre LLM
def analizza_e_rifattorizza_codice(codice, nome_file):
    prompt_per_analisi = gnp.prompt_per_analisi(codice, nome_file)
    #Analisi e rifattorizzazione del codice con Gemini 1.5
    suggerimenti = cmn.comunicazione_gemini_1_5(prompt_per_analisi)
    print(suggerimenti) # Poi da aggiungere a una stringa da passare al frontend
    prompt_per_refactoring = gnp.prompt_per_refactoring(codice, suggerimenti)
    codice_rifattorizzato = cmn.comunicazione_gemini_1_5(prompt_per_refactoring)
    crea_file_in_cartella(codice_rifattorizzato, nome_file, "cartella-gemini-1-5")
    #Analisi e rifattorizzazione del codice con Gemini 2.0
    suggerimenti = cmn.comunicazione_gemini_2_0(prompt_per_analisi)
    print(suggerimenti) # Poi da aggiungere a una stringa da passare al frontend
    prompt_per_refactoring = gnp.prompt_per_refactoring(codice, suggerimenti)
    codice_rifattorizzato = cmn.comunicazione_gemini_2_0(prompt_per_refactoring)
    crea_file_in_cartella(codice_rifattorizzato, nome_file, "cartella-gemini-2-0")
    #Analisi e rifattorizzazione del codice con GPT-4
    suggerimenti = cmn.comunicazione_gpt_4(prompt_per_analisi)
    print(suggerimenti) # Poi da aggiungere a una stringa da passare al frontend
    prompt_per_refactoring = gnp.prompt_per_refactoring(codice, suggerimenti)
    codice_rifattorizzato = cmn.comunicazione_gpt_4(prompt_per_refactoring)
    crea_file_in_cartella(codice_rifattorizzato, nome_file, "cartella-gpt-4")

# Funzione che estrae file di codice da un repository GitHub; la funzione manda i codici agli LLM per analisi e refactoring
def estrai_codici_da_repository(url_repository):
    response = requests.get(url_repository)
    if response.status_code == 200:
        lista_file = response.json()
        for item in lista_file:
            # Controllo se è un file Python, Java, JavaScript, C, C++, C# o PHP
            estensioni = ['.py', '.java', '.js', '.c', '.cpp', '.cs', '.php']
            if item['type'] == 'file' and any(item['path'].endswith(estensione) for estensione in estensioni):
                url_file = item['url']
                file_response = requests.get(url_file)
                if file_response.status_code == 200:
                    file_content = file_response.json()
                    if 'content' in file_content:
                        codice = base64.b64decode(file_content['content']).decode('utf-8')
                        nome_file = os.path.basename(item['path'])
                        analizza_e_rifattorizza_codice(codice, nome_file) # Chiamo funzione per analizzare e rifattorizzare codice
            elif item['type'] == 'dir':
                estrai_codici_da_repository(item['url'])

# Funzione per svuotare le cartelle una volta selezionato "Reset"
def svuota_cartelle():
    percorso_servizi = os.path.dirname(os.path.abspath(__file__))
    percorso_cartella_gemini_1_5 = os.path.join(percorso_servizi, "cartella-gemini-1-5")
    percorso_cartella_gemini_2_0 = os.path.join(percorso_servizi, "cartella-gemini-2-0")
    percorso_cartella_gpt_4 = os.path.join(percorso_servizi, "cartella-gpt-4")
    cartelle = [percorso_cartella_gemini_1_5, percorso_cartella_gemini_2_0, percorso_cartella_gpt_4]
    for cartella in cartelle:
        for file in os.listdir(cartella):
            file_path = os.path.join(cartella, file)
            if os.path.isfile(file_path) and file != ".gitkeep":
                os.remove(file_path)
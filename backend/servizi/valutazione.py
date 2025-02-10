import os
from servizi import generazione_prompt as gnp
from servizi import comunicazione_llm as cmn

def valuta_codici(modello, cartella):
    percorso_cartella = os.path.join(os.path.dirname(os.path.abspath(__file__)), cartella)
    print(f"{cartella} valutata da {modello}:\n")
    files = os.listdir(percorso_cartella)
    for file in files:
        percorso_file = os.path.join(percorso_cartella, file)
        if file != ".gitkeep":
            with open(percorso_file, "r") as f:
                codice_rifattorizzato = f.read()
            nome_file = os.path.basename(percorso_file)
            prompt_per_valutazione = gnp.prompt_per_valutazione(codice_rifattorizzato, nome_file)
            if modello == "Gemini 1.5":
                risposta = cmn.comunicazione_gemini_1_5(prompt_per_valutazione)
                print(risposta)
            elif modello == "Gemini 2.0":
                risposta = cmn.comunicazione_gemini_2_0(prompt_per_valutazione)
                print(risposta)
            elif modello == "GPT-4":
                risposta = cmn.comunicazione_gpt_4(prompt_per_valutazione)
                print(risposta)

def valutazione():
    modelli = ["Gemini 1.5", "Gemini 2.0", "GPT-4"]
    cartelle = ["cartella-gemini-1-5", "cartella-gemini-2-0", "cartella-gpt-4"]
    for modello in modelli:
        for cartella in cartelle:
            valuta_codici(modello, cartella)
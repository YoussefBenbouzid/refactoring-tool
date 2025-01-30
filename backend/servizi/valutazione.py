from servizi import generazione_prompt as gnp
from servizi import comunicazione_llm as cmn
from servizi import interventi_file as inf

def gemini_1_5_valuta_gemini_1_5():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-1-5")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_1_5(prompt)
    return risposta

def gemini_1_5_valuta_gemini_2_0():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-2-0")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_1_5(prompt)
    return risposta

def gemini1_5_valuta_gpt_4():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gpt-4")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_1_5(prompt)
    return risposta

def gemini_2_0_valuta_gemini_1_5():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-1-5")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_2_0(prompt)
    return risposta

def gemini_2_0_valuta_gemini_2_0():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-2-0")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_2_0(prompt)
    return risposta

def gemini_2_0_valuta_gpt_4():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gpt-4")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gemini_2_0(prompt)
    return risposta

def gpt_4_valuta_gemini_1_5():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-1-5")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gpt_4(prompt)
    return risposta

def gpt_4_valuta_gemini_2_0():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gemini-2-0")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gpt_4(prompt)
    return risposta

def gpt_4_valuta_gpt_4():
    codice_rifattorizzato = inf.estrai_codice_da_cartella("cartella-gpt-4")
    prompt = gnp.prompt_per_valutazione(codice_rifattorizzato)
    risposta = cmn.comunicazione_gpt_4(prompt)
    return risposta

def valuta():
    gemini_1_5_valuta_gemini_1_5 = gemini_1_5_valuta_gemini_1_5()
    gemini_1_5_valuta_gemini_2_0 = gemini_1_5_valuta_gemini_2_0()
    gemini_1_5_valuta_gpt_4 = gemini_1_5_valuta_gpt_4()
    gemini_2_0_valuta_gemini_1_5 = gemini_2_0_valuta_gemini_1_5()
    gemini_2_0_valuta_gemini_2_0 = gemini_2_0_valuta_gemini_2_0()
    gemini_2_0_valuta_gpt_4 = gemini_2_0_valuta_gpt_4()
    gpt_4_valuta_gemini_1_5 = gpt_4_valuta_gemini_1_5()
    gpt_4_valuta_gemini_2_0 = gpt_4_valuta_gemini_2_0()
    gpt_4_valuta_gpt_4 = gpt_4_valuta_gpt_4()

    risposta_valutazione = (
        gemini_1_5_valuta_gemini_1_5 + "\n" +
        gemini_1_5_valuta_gemini_2_0 + "\n" +
        gemini_1_5_valuta_gpt_4 + "\n" +
        gemini_2_0_valuta_gemini_1_5 + "\n" +
        gemini_2_0_valuta_gemini_2_0 + "\n" +
        gemini_2_0_valuta_gpt_4 + "\n" +
        gpt_4_valuta_gemini_1_5 + "\n" +
        gpt_4_valuta_gemini_2_0 + "\n" +
        gpt_4_valuta_gpt_4
    )

    return risposta_valutazione
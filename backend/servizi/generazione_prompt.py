import json

# Lettura JSON e recupero definizioni
with open("definizioni/lista_code_smell.json", "r", encoding='utf-8') as file:
    lista_code_smell = json.load(file)

# Lettura JSON e recupero definizioni
with open("definizioni/definizioni_refactoring.json", "r", encoding='utf-8') as file:
    definizioni_refactoring = json.load(file)

# Funzione che genera un prompt dinamicamente con i valori prelevati dai file JSON
def prompt_analisi(codice):
    prompt = f"Ciao, ho bisogno che tu analizzi il seguente codice:\n\n"
    prompt += f"{codice}\n\n"
    prompt += f"Fai riferimento alla seguente lista di code smell e alle relative definizioni:\n"
    for code_smell, data in lista_code_smell.items():
        definizione = data.get("definizione")
        prompt += f"- {code_smell}: {definizione}\n"

    prompt += f"\n"

    prompt += f"Per ogni code smell della lista individuato suggerisci almeno uno tra i refactoring associati nella seguente lista:\n"
    for code_smell, data in lista_code_smell.items():
        refactoring_suggeriti = data.get("refactoring_suggeriti")
        prompt += f"- {code_smell}: {', '.join(refactoring_suggeriti)}\n"

    prompt += f"\n"

    prompt += f"Per ogni refactoring scelto ritorna esattamente la rispettiva definizione presa dalla seguente lista:\n"
    for refactoring, definizione in definizioni_refactoring.items():
        prompt += f"- {refactoring}: {definizione}\n"

    prompt += f"\nLimitati a indicarmi i punti del codice con evidenti code smell e per ognuno di questi indicami i refactoring secondo il seguente modello:\n"

    prompt += f"\n"

    prompt += f"File: [nome del file]\n"
    prompt += f"Code smell individuati: [code smell individuati separati da virgole con relative definizioni tra parentesi]\n"
    prompt += f"Refactoring da applicare: [refactoring da suggerire separati da virgole con relative definizioni tra parentesi]\n"

    prompt += f"\n"

    prompt += f"Sii estremamente sintetico.\n"
    
    return prompt
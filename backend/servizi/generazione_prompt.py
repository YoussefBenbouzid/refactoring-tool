import json

# Lettura JSON e salvataggio valori
with open("definizioni/lista_code_smell.json", "r") as f:
    lista_code_smell = json.load(f)

# Lettura JSON e salvataggio valori
with open("definizioni/definizioni_refactoring.json", "r") as f:
    definizioni_refactoring = json.load(f)

# Funzione che genera un prompt dinamicamente con i valori nei file JSON relativi alle varie definizioni
def genera_prompt(codice):
    prompt = f"Ciao, ho bisogno che tu analizzi il seguente codice:\n"
    prompt += f"{codice}\n"
    prompt += f"Fai riferimento alla seguente list di code smell e alle relative definizioni:\n"
    for code_smell, data in lista_code_smell.items():
        definizione = data.get("definizione")
        prompt += f"- {code_smell}: {definizione}\n"

    prompt += f"Per ogni code smell della lista suggerisci almeno uno tra i refactoring associati nella seguente lista:\n"
    for code_smell, data in lista_code_smell.items():
        refactoring_suggeriti = data.get("refactoring_suggeriti")
        prompt += f"- {code_smell}: {', '.join(refactoring_suggeriti)}\n"

    prompt += f"Per ogni refactoring scelto ritorna anche la rispettiva definizione:\n"
    for refactoring, definizione in definizioni_refactoring.items():
        prompt += f"- {refactoring}: {definizione}\n"
    
    return prompt
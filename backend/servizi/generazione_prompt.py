import json

# Lettura JSON e recupero definizioni code smell
with open("definizioni/lista_code_smell.json", "r", encoding='utf-8') as file:
    lista_code_smell = json.load(file)

# Lettura JSON e recupero definizioni refactoring
with open("definizioni/definizioni_refactoring.json", "r", encoding='utf-8') as file:
    definizioni_refactoring = json.load(file)

# Funzione che genera un prompt che definisce code smell e refactoring da individuare in un codice
def prompt_per_analisi(codice, nome_file):
    prompt = f"Ciao, ho bisogno che tu analizzi il seguente codice:\n\n"
    prompt += f"{codice}\n\n"
    prompt += f"Fai riferimento alla seguente lista di code smell e alle relative definizioni:\n"
    for code_smell, data in lista_code_smell.items():
        definizione = data.get("definizione")
        prompt += f"- {code_smell}: {definizione}\n"
    prompt += f"\nPer ogni code smell della lista individuato suggerisci almeno uno tra i refactoring associati nella seguente lista:\n"
    for code_smell, data in lista_code_smell.items():
        refactoring_suggeriti = data.get("refactoring_suggeriti")
        prompt += f"- {code_smell}: {', '.join(refactoring_suggeriti)}\n"
    prompt += f"\nPer ogni refactoring scelto ritorna esattamente la rispettiva definizione presa dalla seguente lista:\n"
    for refactoring, definizione in definizioni_refactoring.items():
        prompt += f"- {refactoring}: {definizione}\n"
    prompt += f"\nLimitati a indicarmi i code smell e per ognuno di questi indicami i rispettivi refactoring secondo il seguente modello:\n\n"
    prompt += f"File: {nome_file}\n"
    prompt += f"Code smell da risolvere: [code smell individuati separati da virgole con relative definizioni tra parentesi]\n"
    prompt += f"Refactoring da applicare: [refactoring da suggerire separati da virgole con relative definizioni tra parentesi]\n\n"
    prompt += f"Nel caso non dovessero esserci code smell da sistemare o se il codice fosse insensato rispondi secondo il seguente modello:\n\n"
    prompt += f"File: {nome_file}\n"
    prompt += f"Code smell da risolvere: nessun code smell individuato.\n"
    prompt += f"Refactoring da applicare: nessun refactoring da applicare.\n\n"
    prompt += f"Sii estremamente sintetico ed evita ulteriori spiegazioni."
    return prompt

# Funzione che genera un prompt con indicati i refactoring da applicare a un codice
def prompt_per_refactoring(codice, suggerimenti):
    prompt = f"Dato il seguente codice:\n\n"
    prompt += f"{codice}\n\n"
    prompt += f"Riscrivilo facendo riferimento ai seguenti parametri:\n\n"
    prompt += f"{suggerimenti}\n\n"
    prompt += f"Se non dovessero esserci code smell da sistemare o refactoring da applicare allora riscrivi il codice che ti ho passato evitando di modificarlo.\n"
    prompt += f"Sii estremamente sintetico e limitati a scrivere solo il codice senza ulteriori spiegazioni."
    return prompt

# Funzione che genera un prompt per effettuare la valutazione di un codice rifattorizzato
def prompt_per_valutazione(codice, nome_file):
    prompt = f"Ciao, ho bisogno che tu analizzi il seguente codice:\n\n"
    prompt += f"{codice_rifattorizzato}\n\n"
    prompt += f"Fai riferimento alla seguente lista di code smell e alle relative definizioni:\n"
    for code_smell, data in lista_code_smell.items():
        definizione = data.get("definizione")
        prompt += f"- {code_smell}: {definizione}\n"
    prompt += f"\nPer ogni code smell individuato restituiscimi una valutazione secondo il secondo modello (1 è il valore peggiore e 5 il migliore):\n\n"
    prompt += f"Code smell: [nome del code smell individuato]\n"
    prompt += f"Gravità funzionale: [valore numerico da 1 a 5]\n"
    prompt += f"Complessità sintattica: [valore numerico da 1 a 5]\n"
    prompt += f"Livello di ripetizione: [valore numerico da 1 a 5]\n"
    prompt += f"Livello della struttura: [valore numerico da 1 a 5]\n"
    prompt += f"Leggibilità: [valore numerico da 1 a 5]\n\n"
    prompt += f"Metti ogni modello (uno per ogni code smell individuato) uno sotto l'altro nella risposta.\n\n"
    prompt += f"Se non dovessero esserci code smell restituisci la seguente risposta: [Nessun code smell individuato]\n\n"
    prompt += f"Sii estremamente sintetico ed evita ulteriori spiegazioni."
    return prompt
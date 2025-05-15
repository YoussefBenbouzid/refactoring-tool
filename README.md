# Refactoring Tool

## Descrizione
La funzionalità principale del sistema consiste nel refactoring automatico di file di codice di un repository GitHub attraverso il ricorso ai modelli linguistici di grandi dimensioni. In particolare il sistema utilizza i modelli Gemini 1.5, Gemini 2.0 e GPT-4.

Il sistema dispone di un'interfaccia nella quale l'utente può digitare l'url del repository GitHub; il sistema estrae tutti i file e i tre modelli linguistici individuano vari code smell, applicando poi per ognuno di questi i refactoring più appropriati. Ognuno dei tre modelli linguistici genera per ogni file estratto e analizzato un corrispondente file rifattorizzato, il quale viene salvato nella cartella rispettiva. Viene infine effettuata una valutazione incrociata per valutare i vari refactoring applicati.

Il sistema consente di analizzare anche snippet di codice o file di codice, i quali possono essere rispettivamente digitati o allegati dall'utente nell'interfaccia. Il sistema genera un feedback per l'utente nell'interfaccia.

## Implementazione
L'interfaccia è stata realizzata attraverso il framework Bootstrap, combinato insieme ad HTML e CSS, mentre le funzionalità del frontend sono state sviluppate con JavaScript.

Il backend è stato sviluppato in Python, utilizzando in particolare il framework FastAPI, il server Uvicorn e la libreria Pydantic. L'estrazione del codice dal repository GitHub avviene tramite la GitHub REST API, mentre i modelli linguistici sono stati integrati tramite le API e le credenziali rispettive, che sono definite nei file `service_account.json` e `.env`, non mostrati per motivi di sicurezza.

La generazione dei prompt avviene dinamicamente attraverso il caricamento delle definizioni relative ai vari code smell e ai refactoring da file JSON.

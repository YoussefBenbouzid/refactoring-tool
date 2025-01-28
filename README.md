# Refactoring Tool

## Descrizione
La funzionalità principale del sistema consiste nel refactoring automatico di file di codice di un repository GitHub attraverso il ricorso ai modelli linguistici di grandi dimensioni. In particolare il sistema fa riferimento ai modelli Gemini 1.5, Gemini 2.0 e GPT-4.

Il sistema dispone di un'interfaccia nella quale l'utente può digitare l'url del repository GitHub; il sistema estrae tutti i file e i tre modelli linguistici individuano vari code smell, applicando poi per ognuno di questi i refactoring più appropriati. Ognuno dei tre modelli linguistici genera per ogni file estratto e analizzato un corrispondente file rifattorizzato, il quale viene salvato nella cartella rispettiva. Viene infine effettuata una valutazione incrociata per valutare i vari refactoring applicati.

Il sistema consente anche di analizzare anche snippet di codice o file di codice, i quali possono essere rispettivamente digitati o allegati dall'utente nell'interfaccia. Il sistema genera un feedback per l'utente nell'interfaccia.

## Implementazione
La generazione dei prompt viene effettuata dinamicamente attraverso il caricamento delle definizioni relative ai vari code smell e ai refactoring da file JSON. Questo approccio modulare permette di implementare una netta separazione tra la logica e i dati, garantendo una maggiore manutenibilità, scalabilità e flessibilità del sistema.

L'interfaccia è stata realizzata attraverso il framework Bootstrap, combinato ad HTML e CSS, mentre le funzionalità del frontend sono state sviluppate con JavaScript. Il backend è stato sviluppato con il linguaggio Python, in particolare utilizzando il framework FastAPI, il server Uvicorn e la libreria Pydantic. L'estrazione del codice dal repository GitHub viene effettuata con l'ausilio della GitHub REST API.
# Refactoring Tool

## Descrizione
Il sistema consente di analizzare snippet o file di codice sorgente attraverso un prompt a un modello linguistico di grandi dimensioni per identificare una lista predefinita di code smell e per ognuno di questi suggerire i refactoring più adatti.

Il sistema dispone di un'interfaccia nella quale l'utente può caricare gli snippet di codice o alternativamente caricare file sorgente. Una volta inviati, il modello linguistico di grandi dimensioni genera la risposta che viene riportata sullo schermo.

## Implementazione
La generazione del prompt viene effettuata dinamicamente attraverso il caricamento dei dati relativi ai code smell e ai refactoring da file JSON. Questo approccio modulare permette di implementare una netta separazione tra la logica e i dati, garantendo una maggiore manutenibilità, scalabilità e flessibilità del sistema.


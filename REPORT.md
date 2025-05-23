# Relazione sul Progetto: NBA Playoffs 2025

Il progetto sviluppato consiste in un sito web statico che permette di visualizzare i dati relativi alla stagione NBA 2025, con particolare attenzione ai Playoffs. L’obiettivo principale è fornire agli utenti una piattaforma intuitiva e facilmente navigabile per consultare risultati, classifiche e statistiche dettagliate delle squadre e dei giocatori.

## Struttura del Progetto

La struttura del progetto è organizzata in una cartella principale denominata `www`, che contiene i file HTML delle pagine principali (`index.html`, `standings.html`, `playoffs.html`) e una sottocartella per ogni squadra NBA all’interno della directory `teams/`. Ogni squadra ha una propria pagina HTML con il roster e le statistiche aggiornate dei giocatori. Le pagine sono collegate tra loro tramite un sistema di navigazione presente nell’header di ogni pagina.  
La cartella `css/` contiene i fogli di stile CSS che garantiscono un aspetto coerente e moderno a tutte le pagine del sito. 
Le immagini, come il logo NBA, sono raccolte nella cartella `img/`.

## Funzionalità

- **Homepage:** Mostra il calendario delle prossime partite dei Playoffs.
- **Standings:** La pagina `standings.html` presenta le due classifiche di Conference delle squadre aggiornate.
- **Playoffs Bracket:** La pagina `playoffs.html` mostra il tabellone dei Playoffs, con i risultati delle serie.
- **Statistiche Squadre:** Ogni squadra ha una propria pagina (es. `Boston_Celtics.html`), la quale contiene una tabella dettagliata con le statistiche individuali dei giocatori, sia per la stagione regolare sia, per le squadre che li hanno giocati, per i Playoffs.

## Aspetti Tecnici

Il sito è stato realizzato utilizzando HTML e CSS, garantendo massima semplicità, velocità di caricamento e facilità di manutenzione. È stata presa la decisione di utilizzare un solo file PNG (il logo della NBA) e solo quattro file CSS (uno per la home, uno per gli standings, uno per il playoff bracket e uno unico per tutte le pagine di statistica delle squadre) per mantenere la struttura leggera e facilmente caricabile. La struttura modulare permette di aggiornare facilmente i dati delle squadre o aggiungere nuove funzionalità in futuro.

## Conclusioni

Il progetto rappresenta un esempio di sito web informativo, focalizzato sulla chiarezza e sull’accessibilità dei dati sportivi. Può essere facilmente esteso o adattato per altre competizioni sportive o stagioni future. L’organizzazione del codice e dei file facilita la collaborazione e la gestione degli aggiornamenti, rendendo il progetto utile sia a scopo didattico che pratico.
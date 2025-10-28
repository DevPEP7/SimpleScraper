# SimpleScraper v0.3: Il Data Extractor Flessibile

SimpleScraper v0.3 è un potente e flessibile strumento in Python per l'estrazione dati da singole pagine web. Nato come base logica generata da un assistente AI (`AutoDev v0.1`), questo script è stato potenziato per estrarre in modo chirurgico le informazioni che ti servono (titoli, link, contenuti di tag specifici) e salvarle in un file CSV standard.

Ideale per: Analisi SEO, Ricerca di Contenuti, Rilevamento di Link e Archiviazione Dati.

## ✨ Caratteristiche Principali

*   **Estrazione Flessibile:** Specifica tu stesso il tag HTML che vuoi estrarre (`h2`, `p`, `li`, ecc.).
*   **Report Link Completo:** Estrae tutti i link (`<a>` tag) presenti nella pagina.
*   **Output CSV:** Tutti i risultati vengono salvati in un file `scraping_results.csv` per un facile caricamento in Excel o Google Sheets.
*   **Gestione Errori:** Rileva e segnala errori comuni come 404, Timeout o problemi di connessione.

## ⚙️ Prerequisiti

Per eseguire lo scraper, assicurati di avere:

1.  **Python 3.x** installato.
2.  Le librerie necessarie:

```bash

pip install requests beautifulsoup4
🚀 Come Eseguire SimpleScraper v0.3
Scarica il codice sorgente (es. simplescraper_v03.py) da questo repository.
Apri il terminale/prompt dei comandi e naviga nella cartella in cui hai salvato il file.
Esegui il programma: python simplescraper_v03.py
Il programma ti guiderà, chiedendoti l'URL da analizzare e il nome del tag HTML che vuoi estrarre (es. h2).
I risultati verranno stampati a schermo e salvati nel file scraping_results.csv nella stessa directory.
⚠️ Disclaimer Legale ed Etico
Questo strumento è fornito "così com'è" a scopo didattico e di utilità. L'utente è pienamente responsabile del suo utilizzo. Si prega di:
Non violare i termini di servizio dei siti web.
Rispettare il file robots.txt di ciascun sito prima di eseguire qualsiasi operazione automatizzata.
Non sovraccaricare i server con richieste eccessive.
💡 Crediti
Questo progetto è nato dal prompt per la creazione di un assistente AI, AutoDev v0.1, utilizzando l'API Google Gemini.

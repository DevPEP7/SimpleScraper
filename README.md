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
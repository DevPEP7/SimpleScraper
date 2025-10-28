import requests
import csv
from bs4 import BeautifulSoup
import os
from datetime import datetime

# Nome del file CSV per il salvataggio dei risultati
CSV_FILENAME = 'scraping_results.csv'

def save_to_csv(url: str, title: str, custom_tag_name: str, custom_tag_list: list[str], links_list: list[str]):
    """
    Salva i dati estratti (URL, Titolo, Tag Personalizzato, Links) in un file CSV.
    """
    
    # Prepara le stringhe per i campi multipli
    custom_tag_string = ' | '.join(custom_tag_list) if custom_tag_list else f"Nessun <{custom_tag_name}> trovato"
    links_string = ' | '.join(links_list) if links_list else "Nessun link <a> trovato"
    
    # Prepara la riga da scrivere
    new_row = [
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        url,
        title,
        custom_tag_string,
        links_string
    ]
    
    # Intestazione del file CSV: usa il nome del tag scelto dall'utente
    header = ['Timestamp', 'URL', 'Titolo HTML (<title>)', f'Contenuto Tag <{custom_tag_name}>', 'Tutti i Link (<a>)']
    
    try:
        file_exists = os.path.exists(CSV_FILENAME)
        with open(CSV_FILENAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Scrivi l'intestazione solo se il file è nuovo
            if not file_exists:
                writer.writerow(header)
                
            writer.writerow(new_row)
            
        print(f"\n[SUCCESSO] Dati salvati con successo in: {CSV_FILENAME}")
        
    except Exception as e:
        print(f"[ERRORE] Impossibile scrivere il file CSV: {e}")


def simple_scraper_v03():
    """
    Scarica una pagina web, estrae titolo, tag personalizzato e link, e salva in un file CSV.
    """
    url = input("Inserisci l'URL della pagina web da scaricare: ")
    
    # --- NUOVO: Chiedi il tag da cercare ---
    custom_tag_name = input("Quale altro tag HTML vuoi estrarre (es. h2, p, li)? ").strip().lower()
    if not custom_tag_name:
        custom_tag_name = 'h2' # Default se l'utente non inserisce nulla

    try:
        # User-Agent e richiesta
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"Sto scaricando la pagina da: {url}...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Inizializza le variabili per il salvataggio
        page_title = "Nessun titolo (<title>) trovato"
        custom_tag_list = []
        links_list = []

        # --- 1. Estrazione del Titolo HTML (<title>) ---
        title_tag = soup.find('title')
        if title_tag:
            page_title = title_tag.get_text().strip()
        
        print(f"\nRisultati Estratti:")
        print(f"  [TITLE]: {page_title}")

        # --- 2. Estrazione del Tag Personalizzato ---
        custom_tags = soup.find_all(custom_tag_name)
        custom_tag_list = [tag.get_text().strip() for tag in custom_tags if tag.get_text().strip()]
        
        if custom_tag_list:
            print(f"  [{custom_tag_name.upper()} Totali]: {len(custom_tag_list)}")
            for i, item in enumerate(custom_tag_list, 1):
                if i <= 3: 
                    print(f"    -> <{custom_tag_name}> #{i}: {item[:80]}...")
            if len(custom_tag_list) > 3:
                print(f"    ... e altri {len(custom_tag_list) - 3} tag <{custom_tag_name}>.")
        else:
            print(f"  [{custom_tag_name.upper()} Totali]: Nessun tag <{custom_tag_name}> trovato.")

        # --- 3. Estrazione di Tutti i Link (<a>) ---
        link_tags = soup.find_all('a', href=True) # Cerca solo i tag <a> che hanno l'attributo href
        # Estrai solo l'URL (attributo href)
        links_list = [tag['href'] for tag in link_tags] 
        
        print(f"  [LINKS Totali]: {len(links_list)}")
        
        # --- 4. Salvataggio su CSV ---
        save_to_csv(url, page_title, custom_tag_name, custom_tag_list, links_list)

    except requests.exceptions.Timeout:
        print(f"\n[ERRORE] Il tempo massimo per la richiesta a '{url}' è scaduto (Timeout di 15s).")
    except requests.exceptions.ConnectionError:
        print(f"\n[ERRORE] Impossibile connettersi a '{url}'. Controlla la tua connessione internet o l'URL.")
    except requests.exceptions.HTTPError as e:
        print(f"\n[ERRORE] Errore HTTP: {e.response.status_code}. Impossibile scaricare la pagina da '{url}'.")
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRORE] Errore generico durante la richiesta: {e}")
    except Exception as e:
        print(f"\n[ERRORE] Si è verificato un errore inaspettato: {e}")

if __name__ == "__main__":
    simple_scraper_v03()
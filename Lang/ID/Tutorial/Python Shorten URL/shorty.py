from dotenv import load_dotenv
import os
import requests

# Load file .env
load_dotenv()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class ShortenURL:
    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.domain = domain
        self.base_url = 'https://api.short.io/links'

    def shorten_url(self, original_url):
        try:
            response = requests.post(
                self.base_url,
                json={'domain': self.domain, 'originalURL': original_url},
                headers={'authorization': self.api_key, 'content-type': 'application/json'}
            )
            response.raise_for_status()
            data = response.json()
            return data['shortURL']
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

def main():
    api_key = os.getenv('API_KEY')
    domain = os.getenv('DOMAIN')
    original_url = 'https://x.com/hurufnyakecil' # Ganti dengan url yang ingin kamu pendekkan.

    # Cek file .env
    if not api_key or not domain or not original_url:
        print("Your API_KEY or DOMAIN not found in .env file !!")
        return
    
    url_shortener = ShortenURL(api_key, domain)
    short_url = url_shortener.shorten_url(original_url)

    # Jika berhasil
    if short_url:
        clear_terminal()
        print(" ")
        print(f"Original URL: {original_url}")
        print(f"Shortened URL: {short_url}")
        print(f"URL Shortened!")
    else:
        print("Ooppss... Failed to shorten the URL.")

if __name__ == "__main__":
    main()

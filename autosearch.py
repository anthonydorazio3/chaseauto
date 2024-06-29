import requests
from bs4 import BeautifulSoup
import time
import itertools
import random

# List of user agents to choose from
user_agents = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    # Safari
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    # Edge
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
    # Opera
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/78.0.4093.147',
    # Vivaldi
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Vivaldi/4.0',
    # Brave
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/1.27.111',
    # Epic
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Epic/2.0.4',
    # Yandex Browser
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 YaBrowser/21.6.0 Yowser/2.5 Safari/537.36',
    # UC Browser
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 UBrowser/7.0.185.1002 Safari/537.36',
    # Mobile browsers
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0',
    'Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
    # Older versions
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
]

def search(term, engine):
    if engine == 'google':
        url = f'https://www.google.com/search?q={term}'
    elif engine == 'bing':
        url = f'https://www.bing.com/search?q={term}'
    elif engine == 'yandex':
        url = f'https://yandex.com/search/?text={term}'
    
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = soup.find_all('div', class_='g')
    return [result.text for result in results[:5]]

def randeng():
    return random.choices(['google', 'bing', 'yandex'], weights=[3, 2, 1])[0]

def main():
    sterm1 = "Chase Oliver"
    sterm2 = "Mike Ter Maat"
    sterm3 = "Chase Oliver President"
    sterm4 = "Chase Oliver Libertarian"
    sterm5 = "Libertarian President"
    sterm6 = "Chase Oliver President Libertarian"
    
    while True:
        # Choose search term (2:1 ratio)
        current_term = random.choices([sterm1, sterm2, sterm3, sterm4, sterm5, sterm6], weights=[12, 2, 9, 7, 1, 5])[0]
        
        # Choose search engine
        engine = randeng()
        
        print(f"\nSearching {engine} for '{current_term}':")
        results = search(current_term, engine)
        for result in results:
            print(result)
        
        interval = random.randint(11, 19)
        print(f"\nWaiting {interval} seconds before next search...")
        time.sleep(interval)

if __name__ == "__main__":
    main()

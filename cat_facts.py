import requests
import math

def get_first_page():
    url = 'https://catfact.ninja/facts?limit=10'  
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()  

        facts = data.get('data', [])
        if not facts:
            print("Факты о котах не найдены.")
            return

        print("Факты о котах (первая страница):")
        for i, fact in enumerate(facts, start=1):
            print(f"{i}. {fact['fact']}")

    except requests.RequestException as e:
        print("Ошибка:", e)

def get_last_page_and_total(limit=10):
    url = f'https://catfact.ninja/facts?limit=1'  
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        total = data.get('total', 0)
        last_page = math.ceil(total / limit)
        print(f"Общее количество фактов: {total}")
        print(f"Количество фактов на странице: {limit}")
        print(f"Номер последней страницы: {last_page}")
    except requests.RequestException as e:
        print("Ошибка:", e)

def get_last_page_data(limit=10):
    
    url = 'https://catfact.ninja/facts?limit=1'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        total = data.get('total', 0)

        last_page = math.ceil(total / limit)

        last_page_url = f'https://catfact.ninja/facts?limit={limit}&page={last_page}'
        last_page_response = requests.get(last_page_url)
        last_page_response.raise_for_status()
        last_page_data = last_page_response.json()

        facts = last_page_data.get('data', [])
        print(f"Факты на последней странице (страница {last_page}):")
        for i, fact in enumerate(facts, start=1):
            print(f"{i}. {fact['fact']}")
        
        shortest_fact = min(facts, key=lambda x: len(x['fact']))
        print("Самый короткий факт на последней странице:")
        print(shortest_fact['fact'])

    except requests.RequestException as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    get_first_page()
    get_last_page_and_total()
    get_last_page_data(limit=10)
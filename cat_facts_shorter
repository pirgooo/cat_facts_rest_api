import requests, math

limit = 10

def get_first_page():
    resp = requests.get(f'https://catfact.ninja/facts?limit={limit}')
    facts = resp.json().get('data', [])
    print("Факты о котах (первая страница):")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact['fact']}")

def get_total_and_last_page():
    total = requests.get('https://catfact.ninja/facts?limit=1').json()['total']
    last_page = math.ceil(total / limit)
    print(f"\nОбщее количество фактов: {total}")
    print(f"Количество фактов на странице: {limit}")
    print(f"Номер последней страницы: {last_page}")
    return total, last_page

def get_last_page_facts(last_page):
    data = requests.get(f'https://catfact.ninja/facts?limit={limit}&page={last_page}').json()
    facts = data.get('data', [])
    print(f"\nФакты на последней странице (страница {last_page}):")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact['fact']}")
    shortest = min(facts, key=lambda x: len(x['fact']))
    print("\nСамый короткий факт на последней странице:")
    print(shortest['fact'])

if __name__ == '__main__':
    get_first_page()
    total, last_page = get_total_and_last_page()
    get_last_page_facts(last_page)

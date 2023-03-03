from googlesearch import search
import requests
from bs4 import BeautifulSoup

# functie pentru a returna primul paragraf relevant de pe o pagina web
def extract_first_paragraph(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    first_paragraph = soup.find('p')
    if first_paragraph is not None:
        return first_paragraph.text.strip()
    return ""

# functie pentru a cauta raspunsuri la o intrebare folosind Google
def search_google(query):
    results = []
    for url in search(query, stop=50): # cautam primele 50 de rezultate
        paragraph = extract_first_paragraph(url)
        if paragraph:
            results.append(paragraph)
        if len(results) >= 5: # stop daca am adunat 5 raspunsuri relevante
            break
    return results

# bucla infinita pentru a permite utilizatorului să pună întrebări
while True:
    query = input("Intrebare: ")
    if query == "exit":
        break
    answers = search_google(query)
    if answers:
        print(f"Răspuns: {' '.join(answers[0].split()[:50])}...")
    else:
        print("Nu am găsit niciun răspuns relevant.")


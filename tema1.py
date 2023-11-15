"""biblioteca folosita pentru a trimite cereri catre URL specificat
   si de a extrage informatiile din pagina"""
import requests

"""biblioteca folosita pentru a parsa si naviga printre documentele HTML"""
from bs4 import BeautifulSoup


def get_page_info(url):
        """functie folosita pentru trimiterea unor cereri catre URL-ul
        dat de utilizator, extragerea informatiilor cerute din acesta
        si returnarea lor prin 2 obiecte
        parametrul1: url - primeste adresa url de la tastatura """
        response = requests.get(url) #obtinem informatiile paginii

        #parsam continutul html
        soup = BeautifulSoup(response.text, 'html.parser')

        #extragem titlul si descrierea paginii
        title = soup.title.string.strip() if soup.title else "N/A"
        description = soup.find('meta', attrs={'name': 'description'}).get('content').strip() if soup.find('meta',
                                                                                                           attrs={
                                                                                                               'name': 'description'}) else "N/A"

        return title, description

"""se preiau datele introduse de utilizator del a tastatura"""
url = input("Introdu URL-ul paginii: ")

#retinem informatiile in 2 obiecte
title, description = get_page_info(url)

"""afisam datele obtinute sau un mesaj daca
datele nu au putut fi extrase"""
if title and description:
    print(f"\nTitlu paginii: {title}")
    print(f"Descriere: {description}")
else:
    print("Nu s-au putut obține informațiile de la pagină.")

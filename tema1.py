"""biblioteca folosita pentru a trimite cereri catre URL specificat
   si de a extrage informatiile din pagina"""
import requests

"""biblioteca folosita pentru a parsa si naviga printre documentele HTML"""
from bs4 import BeautifulSoup


def page_info(url):
        """functie folosita pentru trimiterea unor cereri catre URL-ul
        dat de utilizator, extragerea informatiilor cerute din acesta
        si returnarea lor prin 2 obiecte
        parametrul1: url - primeste adresa url de la tastatura """
        pagina = requests.get(url) #obtinem informatiile paginii

        #parsam continutul html
        soup = BeautifulSoup(pagina.text, 'html.parser')

        #extragem titlul si descrierea paginii
        titlu = soup.title.string.strip() if soup.title else "N/A"
        descriere = soup.find('meta', attrs={'name': 'descriere'}).get('content').strip() if soup.find('meta',
                                                                                                           attrs={
                                                                                                               'name': 'descriere'}) else "N/A"

        return titlu, descriere

"""se preiau datele introduse de utilizator del a tastatura"""
url = input("Introdu URL-ul paginii: ")

#retinem informatiile in 2 obiecte
titlu, descriere = page_info(url)

"""afisam datele obtinute sau un mesaj daca
datele nu au putut fi extrase"""
if titlu and descriere:
    print(f"\nTitlu paginii: {titlu}")
    print(f"Descriere: {descriere}")
else:
    print("Nu s-au putut obține informațiile de la pagină.")

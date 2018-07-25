import requests
from bs4 import BeautifulSoup

URL_GLOBO_ESPORTE = ('https://globoesporte.globo.com/futebol/times/corinthians/')

r = requests.get(URL_GLOBO_ESPORTE)

soup = BeautifulSoup(r.text, 'lxml')

lista_posts = soup.find_all('div', class_="feed-post bstn-item-shape type-basico")

for lista_post in lista_posts:
    listas = lista_post.find_all('div')
    for lista in listas:
        print(lista.next_element)

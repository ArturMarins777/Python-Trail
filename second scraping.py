from bs4 import BeautifulSoup
import httpx
import lxml

html_text = httpx.get('https://quotes.toscrape.com/')
print(html_text)

soup = BeautifulSoup(html_text.text, 'lxml')
#print(soup.prettify())

quotes = soup.find_all('div', class_ = 'quote')

# Organizando dados em listas
autores = []
for author in quotes:
    author = author.find('small', class_ = "author")
    autores.append(author.get_text(strip=True))
print(autores)

frases = []
for frase in quotes:
  frase = frase.find('span', class_ = 'text')
  frases.append(frase.get_text(strip=True))
print(frases)

tags = []
for tag in quotes:
  tag = tag.find('a', class_ = 'tag')
  tags.append(tag.get_text(strip=True))
print(tags)
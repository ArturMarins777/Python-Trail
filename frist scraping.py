from bs4 import BeautifulSoup
import httpx
import lxml

html_text = httpx.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(html_text.text, 'lxml')

resultado = soup.find_all('div', class_ = 'quote')

for q in resultado:
  print(q.text)
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

target_page = requests.get(url,headers=headers)
soup= BeautifulSoup(target_page.content, 'lxml')

# print(target_page.content)

print(soup.title.get_text())
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
footer = soup.find('footer')
print(str(footer))

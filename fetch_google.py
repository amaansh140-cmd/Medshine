import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
url = "https://www.google.com/search?q=Medii+Derma+Shiine+Clinic+reviews"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

reviews = []
for div in soup.find_all('div'):
    text = div.get_text(separator=' ', strip=True)
    if "star" in text.lower() and len(text) > 30 and "ago" in text.lower():
        reviews.append(text)

with open('scraped_google.txt', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
    f.write("\n--- EXTRACTED ---\n")
    for r in list(set(reviews))[:10]:
        f.write(r + "\n\n")

print("Scraped Google Search for reviews!")

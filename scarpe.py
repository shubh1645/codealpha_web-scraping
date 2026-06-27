import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
all_books = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    all_books.append([title, price])

df = pd.DataFrame(all_books, columns=["Title", "Price"])
df.to_excel("books.xlsx", index = False)
print("successfully saved your file")
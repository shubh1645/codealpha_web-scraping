import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
quotes_data =[]
for quote in soup.find_all("div",class_="quote"):
    text  = quote.find("span", class_= "text").text
    author = quote.find("small", class_="author").text 
    quotes_data.append([text,  author])
    df =pd.DataFrame(quotes_data, columns=["Quote ", "Author"])
    df_sorted = df.sort_values(by="Author", ascending=True)
    df_sorted.to_excel("quotes.xlsx",index=False)
    print("Data saved to quotes.xlsx")
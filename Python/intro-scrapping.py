
# Web Scrapping

from bs4 import BeautifulSoup
import requests

website_address = "http://quotes.toscrape.com"
result = requests.get(website_address)
# print("HTML result is: ", result.text)

soup = BeautifulSoup(result.text, "html.parser")
# print("HTML Formatted text: ", soup)

quotes_list = soup.find_all("div",
                            {"class": "quote"})
# print(len(quotes_list))
# print(quotes_list[0])

for quote in quotes_list:
    quotation = quote.find("span",
                           {"class": "text"})
    print(quotation.text)
    author = quote.find("small",
                        {"class": "author"})
    print(author.text)
    tags_list = quote.find_all("a",
                               {"class":"tag"})
    for tag in tags_list:
        print(tag.text, end=",")
    print()














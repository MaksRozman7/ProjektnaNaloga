from bs4 import BeautifulSoup
import requests

with open("podatkiZaPodjetja.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find_all(class_="card-title")
print(result)








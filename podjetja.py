from bs4 import BeautifulSoup
import requests

with open("podatkiZaPodjetja.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find_all(class_="card-title")


sez=[]
for stvar in doc.find_all(class_="card-title"):
    sez.append(stvar.string.replace(" ","").replace("\n", ""))

print(sez[1:-3])








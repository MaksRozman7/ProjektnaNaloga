from bs4 import BeautifulSoup
import requests

with open("podatkiZaPodjetja.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

result = doc.find_all(class_="card-title")


sez=[]
for stvar in doc.find_all(class_="card-title"):
    sez.append(stvar.string.lstrip().rstrip().replace("\n", ""))


sez.pop(0)
sez.pop(-1)
sez.pop(-1)
sez.pop(-1)



nov_sez = []
nov = ""
for podjetje in sez:
    pod2 = "".join((crka for crka in podjetje if not crka.isdigit()))
    nov_sez.append(pod2)

nov_nov_sez = []
for podjetje in nov_sez:
    pod3 = "".join((znak for znak in podjetje if znak != "."))
    nov_nov_sez.append(pod3)

sez4 = []
for firma in nov_nov_sez:
    fir = firma.strip()
    sez4.append(fir)

print(sez4)







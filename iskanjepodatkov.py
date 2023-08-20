from bs4 import BeautifulSoup
import requests

url = "https://disfold.com/world/companies/?page=1"
rezultat = requests.get(url).text
doc = BeautifulSoup(rezultat, "html.parser")



ime = doc.find_all("h2")


sez = []
for stvar in ime:
    sez.append(stvar.string.lstrip().rstrip().replace("\n", ""))
sez.pop(0)
sez.pop(-1)
sez.pop(-1)
sez.pop(-1)

#print(sez)

nov_sez = []
nov = ""
for podjetje in sez:
    pod2 = "".join((crka for crka in podjetje if not crka.isdigit()))
    nov_sez.append(pod2)


nov_nov_sez = []
for podjetje in nov_sez:
    pod3 = "".join((znak for znak in podjetje if znak != "."))
    nov_nov_sez.append(pod3.strip())

nov_nov_sez.pop(0)

imena_podjetij = nov_nov_sez

ostalo = doc.find_all("td",  )


#print(ostalo)

sez7 = []
for stvar in ostalo:
    sez7.append(stvar)



del sez7[::7]
del sez7[::6]


vrednosti = sez7[0::5]

kratice = sez7[1::5]

države = sez7[2::5]

sektorji = sez7[3::5]

industrije = sez7[4::5]







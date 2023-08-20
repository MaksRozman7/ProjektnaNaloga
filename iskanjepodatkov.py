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

ostalo = doc.find_all("td")


#print(ostalo)

sez7 = []
for stvar in ostalo:
    sez7.append(stvar.text)



del sez7[::7]
del sez7[::6]


vrednosti = sez7[0::5]

kratice = sez7[1::5]

države = sez7[2::5]

sektorji = sez7[3::5]

industrije = sez7[4::5]

vrednosti1 = []
for vrednost in vrednosti:
    vrednosti1.append(vrednost.lstrip().rstrip().replace("\n", ""))

kratice1 = []
for kratica in kratice:
    kratice1.append(kratica.lstrip().rstrip().replace("\n", ""))

države1 = []
for država in države:
    države1.append(država.lstrip().rstrip().replace("\n", ""))

sektorji1 = []
for sektor in sektorji:
    sektorji1.append(sektor.lstrip().rstrip().replace("\n", ""))

industrije1 = []
for industrija in industrije:
    industrije1.append(industrija.lstrip().rstrip().replace("\n", ""))

Vrednosti, Kratice, Države, Sektorji, Industrije = vrednosti1, kratice1, države1, sektorji1, industrije1   

for i in range(len(Sektorji)):
    if Sektorji[i] == "Technology":
        Sektorji[i] = "Tehnologija"

    if Sektorji[i] == "Energy":
        Sektorji[i] = "Energetika"

    if Sektorji[i] == "Communication Services":
        Sektorji[i] = "Komunikacijske storitve"
    
    if Sektorji[i] == "Consumer Discretionary":
        Sektorji[i] = "Potrošniške storitve"
    
    if Sektorji[i] == "Financials":
        Sektorji[i] = "Finance"
    
    if Sektorji[i] == "Healthcare":
        Sektorji[i] = "Zdravstvo"
    
    if Sektorji[i] == "Consumer Staples":
        Sektorji[i] = "Osnovne potrebščine"
    
print(Sektorji)




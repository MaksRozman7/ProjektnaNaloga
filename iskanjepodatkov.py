from bs4 import BeautifulSoup
import requests
import csv

url = "https://disfold.com/world/companies/?page=1"
rezultat = requests.get(url).text
doc = BeautifulSoup(rezultat, "html.parser")

seznam = []

for stran in range(1, 11):
    url = f"https://disfold.com/world/companies/?page={stran}"
    stran = requests.get(url).text
    doc = BeautifulSoup(stran, "html.parser")


    ime = doc.find_all("h2")


    sez = []
    for stvar in ime:
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
        nov_nov_sez.append(pod3.strip())

    nov_nov_sez.pop(0)

    Podjetja = nov_nov_sez

    ostalo = doc.find_all("td")


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
        if len(vrednost) <= 105:
            vrednosti1.append(vrednost.lstrip().rstrip().replace("\n", ""))
        else:
            vred = vrednost[:150]
            vrednosti1.append(vred.lstrip().rstrip().replace("\n", ""))


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
        
        if Sektorji[i] == "Basic Materials":
            Sektorji[i] = "Osnovni materiali"

        if Sektorji[i] == "Industrials":
            Sektorji[i] = "Industrija"

        if Sektorji[i] == "Utilities":
            Sektorji[i] = "Javna služba"
        
        if Sektorji[i] == "Real Estate":
            Sektorji[i] = "Nepremičnine"
        
        


    for i in range(len(Industrije)):
        if Industrije[i] == "Consumer Electronics":
            Industrije[i] = "Potrošniška elektronika"

        if Industrije[i] == "Software—Infrastructure":
            Industrije[i] = "Programska oprema"

        if Industrije[i] == "Oil & Gas Integrated":
            Industrije[i] = "Nafta in plin"
        
        if Industrije[i] == "Internet Content & Information":
            Industrije[i] = "Internetne vsebine in informacije"
        
        if Industrije[i] == "Internet Retail":
            Industrije[i] = "Internetna maloprodaja"
        
        if Industrije[i] == "Semiconductors":
            Industrije[i] = "Polprevodniki"
        
        if Industrije[i] == "Auto Manufacturers":
            Industrije[i] = "Avtomobilska industrija"
        
        if Industrije[i] == "Financial Conglomerates":
            Industrije[i] = "Finančni konglomerat"
        
        if Industrije[i] == "Credit Services":
            Industrije[i] = "Kreditne storitve"
        
        if Industrije[i] == "Household & Personal Products":
            Industrije[i] = "Gospodinjski in osebni izdelki"
        
        if Industrije[i] == "Biotechnology":
            Industrije[i] = "Biotehnologija"
        
        if Industrije[i] == "Luxury Goods":
            Industrije[i] = "Luksuzne dobrine"

        if Industrije[i] == "Banks—Diversified":
            Industrije[i] = "Banke"
        
        if Industrije[i] == "Healthcare Plans":
            Industrije[i] = "Zdravstveno zavarovanje"
        
        if Industrije[i] == "Drug Manufacturers—General":
            Industrije[i] = "Zdravila"
        
        if Industrije[i] == "Discount Stores":
            Industrije[i] = "Trgovine s popusti"
        
        if Industrije[i] == "Home Improvement Retail":
            Industrije[i] = "Oprema za dom"
        
        if Industrije[i] == "Beverages—Non-Alcoholic":
            Industrije[i] = "Brezalkoholne pijače"
        
        if Industrije[i] == "Software—Application":
            Industrije[i] = "Programska oprema"
        
        if Industrije[i] == "Restaurants":
            Industrije[i] = "Restavracije"
        
        if Industrije[i] == "Communication Equipment":
            Industrije[i] = "Komunikaciska oprema"
        
        if Industrije[i] == "Beverages—Wineries & Distilleries":
            Industrije[i] = "Vinarne in destilarne"
        
        if Industrije[i] == "Semiconductor Equipment & Materials":
            Industrije[i] = "Polprevodniška oprema in materiali"
    
 
    for i in range(len(Države)):
        if Države[i] == "United States":
            Države[i] = "ZDA"

        if Države[i] == "Saudi Arabia":
            Države[i] = "Savdska Arabija"

        if Države[i] == "Taiwan":
            Države[i] = "Tajvan"
        
        if Države[i] == "France":
            Države[i] = "Francija"
        
        if Države[i] == "China":
            Države[i] = "Kitajska"
        
        if Države[i] == "South Korea":
            Države[i] = "Južna Koreja"

        if Države[i] == "Denmark":
            Države[i] = "Danska"
        
        if Države[i] == "Netherlands":
            Države[i] = "Nizozemska"
        
        if Države[i] == "Switzerland":
            Države[i] = "Švica"
        
        if Države[i] == "United Kingdom":
            Države[i] = "Združeno kraljestvo" 
        
        if Države[i] == "Ireland":
            Države[i] = "Irska"
        
        if Države[i] == "Germany":
            Države[i] = "Nemčija"
        
        if Države[i] == "Australia":
            Države[i] = "Avstralija"

        if Države[i] == "Canada":
            Države[i] = "Kanada"
        
        if Države[i] == "India":
            Države[i] = "Indija"
        
        if Države[i] == "Spain":
            Države[i] = "Španija"
        
        if Države[i] == "Belgium":
            Države[i] = "Belgija"
        
        if Države[i] == "Japan":
            Države[i] = "Japonska"
        
        if Države[i] == "Russia":
            Države[i] = "Rusija"
        
        if Države[i] == "Brazil":
            Države[i] = "Brazilija"

        if Države[i] == "Norway":
            Države[i] = "Norveška"
        
        if Države[i] == "Austria":
            Države[i] = "Avstrija"
        
        if Države[i] == "Indonesia":
            Države[i] = "Indonezija"
        
        if Države[i] == "Mexico":
            Države[i] = "Mehika"
        
        if Države[i] == "Sweden":
            Države[i] = "Švedska"
        
        if Države[i] == "Singapore":
            Države[i] = "Singapur"
        
        if Države[i] == "Italy":
            Države[i] = "Italija"

        if Države[i] == "Canada":
            Države[i] = "Kanada"
        
        if Države[i] == "India":
            Države[i] = "Indija"
        
        if Države[i] == "Spain":
            Države[i] = "Španija"
        
        if Države[i] == "Belgium":
            Države[i] = "Belgija"
        
        if Države[i] == "Thailand":
            Države[i] = "Tajska"
        
        if Države[i] == "South Africa":
            Države[i] = "Južna Afrika"

          





    
    for i in range(50):
        seznam.append({'ime': Podjetja[i], 'država': Države[i], 'kratica': Kratice[i], 'vrednost': Vrednosti[i], 'sektor': Sektorji[i], 'industrija': Industrije[i]})

    with open("podatkiPodjetja.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ime", "država", "kratica", "vrednost", "sektor", "industrija"])
        for firma in seznam:
            writer.writerow([firma["ime"], firma["država"], firma["kratica"], firma["vrednost"], firma["sektor"], firma["industrija"]])
    
    #print(Vrednosti)      
   
    
    

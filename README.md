# ProjektnaNaloga - Analiza 500 najvrednejših podjetij na trgu

Avtor : Maks Rozman

Za projektno nalogo pri UVP sem napisal program za analizo podatkov. S spletne strani [Disfold.com](https://disfold.com/world/companies/?page=1) sem uvozil html in iz njega izluščil podatke o 500 najvrednejših podjetjih. Ti podatki so:
1. Ime podjetja
2. Država, kjer je podjetje registrirano
3. Oznaka delnice
4. Tržna vrednost podjetja
5. Sektor v katerega spada podjetje
6. Industrija v katero spada podjetje


Ker ZDA veljajo za gospodarsko velesilo, me je zanimalo v kolikšni meri to drži. Zato sem preveril kakšen tržni delež imajo njihova podjetja in pa koliko so vredna v primerjavi z ostalimi državami. Prav tako sem želel vedeti, kakšna so razmerja moči med različnimi sektorji in industrijami. Preveril sem še, ali so kakšna opazna izstopanja iz povprečja, kar se tiče vrednosti podjetij glede na sektor. Za konec pa sem pogledal porazdelitev podjetij glede na vrednost.

Vse vrednosti so v milijardah dolarjev.
Podatki so iz 1-7-2023.


## Navodila za uporabo
V datoteki iskanjepodatkov.py je koda za pridobivanje in urejanje podatkov s spletne strani. V urejanje.py sem podatke pogrupiral v želene skupine, v grafi.py pa narisal potrebne grafe. Končni izsledki so predstavljeni v predstavitev.ipynb.

Uporabnik lahko prebere zgolj jupyter datoteko, če pa želi pognati program, pa mora prenesti podatke iz določenih datotek in pa knjižnjice. Kaj točno je potrebno je navedeno na začetku predstavitev.ipynb.

V repozitoriju so dodani tudi csv-ji, če koga to zanima oziroma jih potrebuje. Glavni csv z vsemi podatki je podatkiPodjetja.csv, ostali pa so podatki, uporabljeni za grafe.

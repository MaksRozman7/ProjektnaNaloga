import pandas as pd

podjetja = pd.read_csv("podatkiPodjetja.csv")

pd.options.display.max_rows = 20



firme_po_državah = podjetja.groupby("država").agg({"ime": "count", "vrednost": "sum"})

skupna_vrednost_držav = firme_po_državah.sort_values("vrednost", ascending=False)

podjetja_na_državo = firme_po_državah.sort_values("ime", ascending=False)
    
sektor_vrednosti = podjetja.groupby("sektor").agg({"ime": "count", "vrednost": "sum"}).sort_values("vrednost", ascending=False)

sektor_povprečna_vrednost = podjetja.groupby("sektor")["vrednost"].mean().sort_values(ascending=False)

print(sektor_povprečna_vrednost)
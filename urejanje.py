import pandas as pd

podjetja = pd.read_csv("podatkiPodjetja.csv")

pd.options.display.max_rows = 20



vrednost_po_državah = podjetja.groupby("država").agg({"vrednost": "sum"})

število_po_državah = podjetja.groupby("država").agg({"ime": "count"})

vrednost_države = vrednost_po_državah.sort_values("vrednost", ascending=False).round(2)

št_podjetij_na_državo = število_po_državah.sort_values("ime", ascending=False)
    
vrednosti_sektorjev = podjetja.groupby("sektor").agg({"vrednost": "sum"}).sort_values("vrednost", ascending=False).round(2)

povprečna_vrednost_sektorja = podjetja.groupby("sektor")["vrednost"].mean().sort_values(ascending=False).round(2)




vrednost_države.to_csv("vrednost_države.csv")

št_podjetij_na_državo.to_csv("št_podjetij_na_državo.csv")

vrednosti_sektorjev.to_csv("vrednosti_sektorjev.csv")

povprečna_vrednost_sektorja.to_csv("povprečna_vrednost_sektorja.csv")

    
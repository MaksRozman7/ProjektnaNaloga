import pandas as pd

podjetja = pd.read_csv("podatkiPodjetja.csv")

pd.options.display.max_rows = 20



porazdelitev_držav = podjetja.država.value_counts()

vrednost_po_državah = podjetja.groupby("država").agg({"vrednost": "sum"})

vrednost_države = vrednost_po_državah.sort_values("vrednost", ascending=False).round(2)


porazdelitev_sektorjev = podjetja.sektor.value_counts()

vrednosti_sektorjev = podjetja.groupby("sektor").agg({"vrednost": "sum"}).sort_values("vrednost", ascending=False).round(2)

povprečna_vrednost_sektorja = podjetja.groupby("sektor")["vrednost"].mean().sort_values(ascending=False).round(2)


porazdelitev_industrij = podjetja.industrija.value_counts()




porazdelitev_držav.to_csv("porazdelitev_držav.csv")  
vrednost_države.to_csv("vrednost_države.csv")


porazdelitev_sektorjev.to_csv("porazdelitev_sektorjev.csv")
vrednosti_sektorjev.to_csv("vrednosti_sektorjev.csv")
povprečna_vrednost_sektorja.to_csv("povprečna_vrednost_sektorja.csv")


porazdelitev_industrij.to_csv("porazdelitev_industrij.csv")


import matplotlib.pyplot as plt
import seaborn as sns

from urejanje import porazdelitev_sektorjev, porazdelitev_držav, vrednost_države, povprečna_vrednost_sektorja, vrednosti_sektorjev, porazdelitev_industrij
from urejanje import podjetja


plt.pie(porazdelitev_držav, radius=1.2, autopct="%0.2f%%")
plt.title("Odstotek podjetij na državo")
plt.legend(labels=podjetja.država.unique(), loc='upper left', bbox_to_anchor=(1.1, 1.1))
plt.show()



vrednost_države = vrednost_države[:10]
ax = vrednost_države.plot(kind='bar')
ax.set_xlabel('Država', fontsize=12)
ax.set_ylabel('Skupna vrednost podjetij (mrd.)', fontsize=12)
plt.title("Skupna vrednost podjetij (top 10)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
porazdelitev_sektorjev.plot(kind='bar', color=["pink", "blue", "grey", "purple", "green", "red", "brown", "orange", "olive", "cyan", "black"])
plt.title("Število podjetij v določenem sektorju")
plt.xlabel("Sektor")
plt.ylabel("Število podjetij")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

ax = vrednosti_sektorjev.plot(kind='bar')
ax.set_xlabel('Sektor', fontsize=12)
ax.set_ylabel('Vrednost (mrd.)', fontsize=12)
plt.title("Vrednost sektorjev")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
povprečna_vrednost_sektorja.plot(kind='bar', color=["blue", "orange", "green", "red", "purple", "brown", "pink", "grey", "olive", "cyan", "black"])
plt.title("Povprečna vrednost sektorja")
plt.xlabel("Sektor")
plt.ylabel("Vrednost (mrd.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
porazdelitev_industrij = porazdelitev_industrij[:15]
porazdelitev_industrij.plot(kind='bar', color=["blue", "orange", "green", "red", "purple", "brown", "pink", "grey", "olive", "cyan", "black", "gold", "hotpink", "darkviolet", "mediumblue"])
plt.title("15 največjih industrij")
plt.xlabel("Industrija")
plt.ylabel("Število podjetij")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


sns.scatterplot(data=podjetja, x='vrednost', y='sektor')
plt.title("Povezava med sektorjem in vrednostjo podjetja")
plt.xlabel("Vrednost(mrd.)")
plt.ylabel("Sektor")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(podjetja['vrednost'], bins=15, color=["purple"])
plt.title("Histogram vrednosti podjetij")
plt.xlabel("Vrednost(mrd.)")
plt.ylabel("Število podjetij")
plt.tight_layout()
plt.show()
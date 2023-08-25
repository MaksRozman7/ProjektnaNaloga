import matplotlib.pyplot as plt

from urejanje import porazdelitev_sektorjev

plt.figure(figsize=(12, 6))
porazdelitev_sektorjev.plot(kind='bar')
plt.title("Število podjetij v določenem sektorju")
plt.xlabel("Sektorji")
plt.ylabel("Število")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
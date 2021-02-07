merkkijono = input("Anna merkkijono: ")
osajono = input("Anna osajono: ")
osajonoPituus = len(osajono)
kohta = merkkijono.find(osajono)
luku = kohta+osajonoPituus
merkkijono = merkkijono[kohta+osajonoPituus:]
kohta = merkkijono.find(osajono)
if kohta != -1:
    print(f"Osajonon toinen esiintymä on kohdassa {luku+kohta}.")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")

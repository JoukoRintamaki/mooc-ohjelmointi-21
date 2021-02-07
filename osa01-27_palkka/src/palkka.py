tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = int(input("Työtunnit: "))
viikonpaiva = input("Viikonpäivä: ")

palkka = tuntipalkka*tyotunnit
if viikonpaiva == "sunnuntai":
    palkka *= 2

print(f"Palkka {palkka} euroa")

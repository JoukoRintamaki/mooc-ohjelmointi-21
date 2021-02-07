merkkijono = input("Anna sana: ")
if merkkijono[1] == merkkijono[len(merkkijono)-2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {merkkijono[1]}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")

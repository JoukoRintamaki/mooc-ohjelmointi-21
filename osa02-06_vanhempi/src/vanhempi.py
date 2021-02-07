print("Henkilö 1:")
henkilo1Nimi = input("Nimi: ")
henkilo1Ika = int(input("Ikä: "))
print("Henkilö 2:")
henkilo2Nimi = input("Nimi: ")
henkilo2Ika = int(input("Ikä: "))
if(henkilo1Ika > henkilo2Ika):
    print(f"Vanhempi on {henkilo1Nimi}")
elif(henkilo1Ika < henkilo2Ika):
    print(f"Vanhempi on {henkilo2Nimi}")
else:
    print(f"{henkilo1Nimi} ja {henkilo2Nimi} ovat yhtä vanhoja")

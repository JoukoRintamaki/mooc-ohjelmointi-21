def pisteetHarjoituksista(harjoitustenMaara):
    if harjoitustenMaara < 10:
        harjoituspisteet = 0
    elif 10 <= harjoitustenMaara < 20:
        harjoituspisteet = 1
    elif 20 <= harjoitustenMaara < 30:
        harjoituspisteet = 2
    elif 30 <= harjoitustenMaara < 40:
        harjoituspisteet = 3
    elif 40 <= harjoitustenMaara < 50:
        harjoituspisteet = 4
    elif 50 <= harjoitustenMaara < 60:
        harjoituspisteet = 5
    elif 60 <= harjoitustenMaara < 70:
        harjoituspisteet = 6
    elif 70 <= harjoitustenMaara < 80:
        harjoituspisteet = 7
    elif 80 <= harjoitustenMaara < 90:
        harjoituspisteet = 8
    elif 90 <= harjoitustenMaara < 100:
        harjoituspisteet = 9
    elif harjoitustenMaara == 100:
        harjoituspisteet = 10
    return harjoituspisteet


def arvosana(pisteet):
    if 0 <= pisteet <= 14:
        arvosana1 = 0
    elif 15 <= pisteet <= 17:
        arvosana1 = 1
    elif 18 <= pisteet <= 20:
        arvosana1 = 2
    elif 21 <= pisteet <= 23:
        arvosana1 = 3
    elif 24 <= pisteet <= 27:
        arvosana1 = 4
    elif 28 <= pisteet <= 30:
        arvosana1 = 5
    return arvosana1

def kaavio (taulukko: list):
    i = 5
    while i >= 0:    
        print(i,": ","*"*taulukko[i],sep="")
        i -= 1

def tilasto (arvosanat: list):
    print ("Tilasto:")
    print ("Pisteiden keskiarvo:", sum(pisteTaulukko)/len(pisteTaulukko))
    prosentti=f"{(((sum(arvosanaTaulukko) - arvosanaTaulukko[0]) / sum(arvosanaTaulukko))*100):.1f}"
    print ("Hyväksymisprosentti:", prosentti)
    print ("Arvosanajakauma:")
    kaavio(arvosanat)

arvosanaTaulukko = [0,0,0,0,0,0]
pisteTaulukko = []
while True:
    syote = input("Koepisteet ja harjoitusten määrä: ")
    if syote == "":
        tilasto(arvosanaTaulukko)
        break
    else:
        koepisteet = int(syote.split(" ")[0])
        harjoitustenMaara = int(syote.split(" ")[1])
        pisteTaulukko.append(pisteetHarjoituksista(harjoitustenMaara)+koepisteet)
        if koepisteet >= 10:
            arvosanaFinal = arvosana(pisteetHarjoituksista(harjoitustenMaara)+koepisteet)
            arvosanaTaulukko[arvosanaFinal] += 1
        else:
            arvosanaFinal = 0
            arvosanaTaulukko[arvosanaFinal] += 1
        

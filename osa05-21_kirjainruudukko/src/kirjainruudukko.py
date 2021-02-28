import string
kerrokset = int(input("Kerrokset: "))
aakkoset = list(string.ascii_uppercase)
kuvionLeveys = kerrokset*2-1
kirjain = kerrokset-1

kuvio = [[""]*kuvionLeveys for i in range(kuvionLeveys)]
j = 0
while kuvionLeveys > 0:
    for i in range(j, kuvionLeveys):
        kuvio[j][i] = aakkoset[kirjain]
        kuvio[i][kuvionLeveys-1] = aakkoset[kirjain]
        kuvio[i][j] = aakkoset[kirjain]
        kuvio[kuvionLeveys-1][i] = aakkoset[kirjain]
    kuvionLeveys -= 1
    j += 1
    kirjain -= 1

for rivi in kuvio:
    for merkki in rivi:
        print(merkki, end="")
    print()

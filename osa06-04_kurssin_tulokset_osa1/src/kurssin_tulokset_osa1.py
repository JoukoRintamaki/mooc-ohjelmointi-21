if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

rekisteri = {}
with open(opiskelijatiedot) as opiskelijatiedot:
    for rivi in opiskelijatiedot:
        opiskelija = {}
        if rivi.split(";")[0] == "opnro":
            continue
        opiskelija["etunimi"] = rivi.split(";")[1].strip()
        opiskelija["sukunimi"] = rivi.split(";")[2].strip()
        rekisteri[rivi.split(";")[0]] = opiskelija

with open(tehtavatiedot) as tehtavatiedot:
    for rivi in tehtavatiedot:
        if rivi.split(";")[0] == "opnro":
            continue
        rekisteri[rivi.split(";")[0]]["tehtavatiedot"] = list(
            map(int, rivi.split(";")[1:]))


for opiskelija, tiedot in rekisteri.items():
    print(tiedot["etunimi"], tiedot["sukunimi"], sum(tiedot["tehtavatiedot"]))

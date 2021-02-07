lista = []
i=0
while True:
    sana=input("sana: ")
    if (sana not in lista):
        lista.append(sana)
        i += 1
    else:
        print (f"Annoit {i} eri sanaa")
        break
        
lause = ""
tupla = ""
while True:
    sana = input("Anna sana: ")    
    if sana != "loppu" and tupla != sana:
        lause += " " + sana
        tupla = sana
    else:
        break
print(lause)
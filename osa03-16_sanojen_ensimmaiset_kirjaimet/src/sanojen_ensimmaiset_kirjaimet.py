lause = input("Anna lause: ")
kohta = 0
while True:
    print(lause[kohta])
    lause = lause[kohta+1:]
    kohta = lause.find(" ")
    if kohta == -1:
        break
    else:
        kohta += 1

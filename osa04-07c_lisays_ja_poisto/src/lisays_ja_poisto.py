lista = []
while True:
    print(f"Lista on nyt {lista}")
    syote = input("(l)isää, (p)oista vai e(x)it:")
    if syote == "l":
        lista.append(len(lista)+1)
    elif syote == "p":
        lista.pop(-1)
    else:
        print("Moi!")
        break

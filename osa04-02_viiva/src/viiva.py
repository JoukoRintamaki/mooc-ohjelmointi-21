def viiva(pituus, merkki):
    if merkki == "":
        print("*"*pituus)
    else:
        print(merkki[0]*pituus)


if __name__ == "__main__":
    viiva(5, "x")

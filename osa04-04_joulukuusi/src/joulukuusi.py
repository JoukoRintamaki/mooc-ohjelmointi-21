def joulukuusi(koko):
    print("joulukuusi!")
    rivi = koko
    maara=1
    tyhjaa=koko-1
    while rivi > 0:        
        print(" "*tyhjaa+"*"*maara)
        rivi -= 1
        maara += 2
        tyhjaa -= 1
    tyhjaa=koko-1
    print(" "*tyhjaa+"*")


if __name__ == "__main__":
    joulukuusi(5)

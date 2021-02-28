def lukukirja():
    sanakirja = {}
    sanakirja[0] = "nolla"
    sanakirja[1] = "yksi"
    sanakirja[2] = "kaksi"
    sanakirja[3] = "kolme"
    sanakirja[4] = "neljä"
    sanakirja[5] = "viisi"
    sanakirja[6] = "kuusi"
    sanakirja[7] = "seitsemän"
    sanakirja[8] = "kahdeksan"
    sanakirja[9] = "yhdeksän"
    sanakirja[10] = "kymmenen"
    for i in range(1, 10):
        sanakirja[i+10] = sanakirja[i]+"toista"
    for i in range(2, 10):
        sanakirja[i*10] = sanakirja[i]+"kymmentä"
    for i in range(2, 10):
        for j in range(1, 10):
            sanakirja[i*10+j] = sanakirja[i*10]+sanakirja[j]

    return sanakirja

if __name__ == "__main__":
    luvut = lukukirja()    
    for i in range(0,100):
        print(luvut[i])
    #print(luvut[2])
    #print(luvut[11])
    #print(luvut[45])
    #print(luvut[99])
    #print(luvut[0])

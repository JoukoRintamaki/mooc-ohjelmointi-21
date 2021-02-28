def histogrammi(merkkijono: str):
    analyysi={}
    for merkki in merkkijono:
        if merkki not in analyysi:
            analyysi[merkki]=0
        analyysi[merkki] += 1
    for avain, arvo in analyysi.items():
        print(avain,"*"*arvo)
def nelio(sana, b):
    if(len(sana)) == 0:
        return
    merkkijono = sana*int(b*b/len(sana)+1)
    i = b
    a = 0
    while i > 0:
        print(merkkijono[a:a+b])
        a += b
        i -= 1


if __name__ == "__main__":
    nelio("", 3)

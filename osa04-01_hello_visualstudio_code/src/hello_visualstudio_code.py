while True:
    editor = (input("Editori: ")).lower()
    if editor in ("word","notepad"):
        print("surkea")
    elif editor == ("Visual Studio Code").lower():
        print("loistava valinta!")
        break
    else:
         print ("ei ole hyvä")


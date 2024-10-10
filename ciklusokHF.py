import beolvas

def tizennegy():
    # 14. Add össze 10 bekért számnál a negatív számokat!
    osszeg = 0
    for i in range(1,11):
        print("Add meg a(z) " + str(i) + ". számot! ", end="")
        szam = beolvas.tortSzamBeolvas2()
        if szam < 0:
            osszeg = osszeg + szam

    print("A megadott számokból a negatívok összege: " + str(osszeg))

def tizenot():
    # 15. Kérj be számot mindaddig, amíg negatív és 3-mal osztható nem lesz!
    szam = beolvas.tortSzamBeolvas()
    while not( (szam%3==0) and (szam<0) ):
        print("A megadott szám nem negatív és nem osztható 3-mal!")
        szam = beolvas.tortSzamBeolvas()
    print("A megadott szám negatív és osztható 3-mal!")

def tizenhat():
    # 16. Kérj be számot mindaddig, amíg 3 jegyű pozitív szám nem lesz!
    szam = beolvas.tortSzamBeolvas()
    while not( (szam>=100) and (szam<1000) and (szam.is_integer()) ):
        print("A megadott szám nem pozitív 3 jegyű!")
        szam = beolvas.tortSzamBeolvas()
    print("A megadott szám pozitív 3 jegyű!")

def tizennyolc():
    # 18. Kérj be 5 szöveget, és fűzd őket össze space-szel, majd írasd ki a kész szöveget!
    szoveg = ""
    for i in range(5):
        szoveg = szoveg + beolvas.szovegBeolvas() + " "
    print (szoveg)

def husz():
    # 20. Kérj be 5 számot, és döntsd el, hogy van-e köztük páros!
    paros = False
    for i in range(5):
        szam = beolvas.tortSzamBeolvas()
        if (szam%2 == 0) and (szam != 0):
            paros = True
    if paros:
        print("A bekért számok közt van páros.")
    else:
        print("A bekért számok közt nincs páros.")

def huszonegy():
    # 21. Kérj be 5 számot, és döntsd el, hogy van-e köztük páros, majd ezt a számot add is meg, ha van ilyen!
    paros = ""
    for i in range(5):
        szam = beolvas.tortSzamBeolvas()
        if (szam%2 == 0) and (szam != 0):
            paros = paros + str(szam) + " "
    if paros != "":
        print("Páros számok: " + paros)
    else:
        print("Nincs páros szám a megadottak közt")
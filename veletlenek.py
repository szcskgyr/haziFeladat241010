import beolvas

def kettoB():
    szam = beolvas.egeszSzamBeolvas()
    while (szam < 1) or (szam > 12):
        print("A megadott szám rossz!")
        szam = beolvas.egeszSzamBeolvas()

    szam = round(szam, 0)
    if szam == 1:
        print("január")
    elif szam == 2:
        print("február")
    elif szam == 3:
        print("március")
    elif szam == 4:
        print("április")
    elif szam == 5:
        print("május")
    elif szam == 6:
        print("június")
    elif szam == 7:
        print("július")
    elif szam == 8:
        print("augusztus")
    elif szam == 9:
        print("szeptember")
    elif szam == 10:
        print("október")
    elif szam == 11:
        print("november")
    else:
        print("december")

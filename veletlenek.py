import beolvas

def kettoB():
    # 2. A program  olvasson be a konzolról egy egész számot! Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma! A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba (1-nél kisebb vagy 12-nél nagyobb szám) esetén legyen hibaüzenet!
    # b. Ellenőrzötten csak 1 és 12 közötti számot fogadunk el a bekérés során!
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

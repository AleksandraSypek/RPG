import src.Spotkanie
import pickle
import src.Przeciwnik
import random
import os
with open("tmp","rb") as f_temp:
    sejw = pickle.load(f_temp)

with open(sejw, "rb") as f:
    bohater = pickle.load(f)
bohater.obecnyPoziom = 1

def walka(bohater, przeciwnik):
    print("Walczysz z " + przeciwnik.imie)
    print("Rzucasz zaklęcie")
    for x in range (0,3):
        zaklecieBohater = random.randint(1,6)
        print("\n"+ str(zaklecieBohater) + " to siła Twojego zaklęcia")
        zakleciePrzeciwnik = random.randint(1,6)
        print(str(zakleciePrzeciwnik) + " to siła zaklęcia przeciwnika")
        if zakleciePrzeciwnik < zaklecieBohater:
            print("Ale mu uderzyłeś")
            przeciwnik.zdrowie = przeciwnik.zdrowie - zaklecieBohater
        elif zakleciePrzeciwnik > zaklecieBohater:
            print("Dostałeś w twarz")
            bohater.zdrowie = bohater.zdrowie - zakleciePrzeciwnik
        else:
            print("Nie trafiłeś")
    print("\nKoniec walek. Twój stan zdrowia: " + str(bohater.zdrowie))
    with open("save.obj", "wb", ) as file_hero:
        pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL)


print('Znajdujesz się na ostatnim poziomie. Aby skończyć grę musisz wykonać 15 zadań ')
pokoje = {
    0 : {"nazwa" : "Korytarz", "północ" : 1, "wschód" : 2, "południe" : 3, "zachód" : 4},
    1 : {"nazwa" : "Sowy", "południe" : 0},
    2 : {"nazwa" : "Bank", "zachód" : 0 },
    3 : {"nazwa" : "Olivander", "północ" : 0 },
    4 : {"nazwa" : "Quiditch", "wschód" : 0 }
}

obecnyPokoj = 0
print("Wybierz komendę:")
print("> idz [kierunek]")
print("> zrob - zaczyna interakcje")
print("> pomoc - wyswietla pomoc")
print("> pokaz - pokazuje statystyki gracza")
print("> menu - wychodzi do menu")
print("W każdej z lokacji możesz podać komendę \"zrob1\" lub \"zrob 2\"")

while True:
    if bohater.wykonaneZadania > 14:
        print("Wygrałeś kurła")
        os.system("Wygrana.py")
    else:
        if bohater.zdrowie <= 0:
            print("Gejm ołwer")
            os.system("Menu.py")

        print("\nJesteś obecnie w " + pokoje[obecnyPokoj]["nazwa"])
        ruch = input("> ").lower().split()
        if ruch[0] == "pokaz":
            with open("save.obj", "rb") as f:
                bohater = pickle.load(f)
            bohater.show()
        if ruch[0] == "idz":
            if ruch[1] in pokoje[obecnyPokoj]:
                obecnyPokoj = pokoje[obecnyPokoj][ruch[1]]
            else:
                print("Nie mozesz tam isc")

        if ruch[0] == "zrob":
            if  pokoje[obecnyPokoj]["nazwa"] == "Sowy":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().sowy()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().bank()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Korytarz":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().korytarz()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()


            if pokoje[obecnyPokoj]["nazwa"] == "Bank":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().bank()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Quiditch":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().quiditch()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()
            if pokoje[obecnyPokoj]["nazwa"] == "Olivander":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().olivander()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

        if ruch[0] == "pomoc":
            lista = []
            print("Możesz udać się na:")
            for key, values in pokoje[obecnyPokoj].items():
                lista.append(key) #dopisuje kierunki swiata do listy
            for x in range (1,len(pokoje[obecnyPokoj])):
                print(lista[x])#wypisuje kierunki swiata w ktore moge pojsc

        if ruch[0] == "wyjdz":
            print("Opuszczasz grę!")
            break
        if ruch[0] != "idz" and ruch[0] != "pomoc" and ruch[0] != "zrob" and ruch[0] != "wyjdz" and ruch[0] != "pokaz":
            print("Zła komenda")



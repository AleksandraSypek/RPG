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

def walka(bohater, przeciwnik):            #funkcja
    print("Walczysz z " + przeciwnik.imie)
    print("Rzucasz zaklęcie")
    for x in range (0,3):              #pętla
        zaklecieBohater = random.randint(1,6)
        print("\n"+ str(zaklecieBohater) + " to siła Twojego zaklęcia")
        zakleciePrzeciwnik = random.randint(1,6)
        print(str(zakleciePrzeciwnik) + " to siła zaklęcia przeciwnika")
        if zakleciePrzeciwnik < zaklecieBohater:
            print("Ale go uderzyłeś")
            przeciwnik.zdrowie = przeciwnik.zdrowie - zaklecieBohater
        elif zakleciePrzeciwnik > zaklecieBohater:
            print("Dostałeś w twarz")
            bohater.zdrowie = bohater.zdrowie - zakleciePrzeciwnik
        else:
            print("Nie trafiłeś")
    print("\nKoniec walek. Twój stan zdrowia: " + str(bohater.zdrowie))
    bohater.wykonaneZadania = bohater.wykonaneZadania +1
    with open(sejw, "wb", ) as file_hero:
        pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL)                   #zapis pliku


print('Znajdujesz się na poziomie 1. Aby wejsc na kolejny poziom musisz wykonać 5 zadań ')
pokoje = {
    0 : {"nazwa" : "Korytarz", "północ" : 1, "wschód" : 2, "południe" : 3, "zachód" : 4},
    1 : {"nazwa" : 'Latanie', "południe" : 0}, # slownik
    2 : {"nazwa" : "Numerologia", "zachód" : 0 },
    3 : {"nazwa" : "Walka", "północ" : 0 },
    4 : {"nazwa" : "Bank", "wschód" : 0 }
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
    if bohater.wykonaneZadania > 4:
        os.system("Poziom2.py")
    else:
        if bohater.zdrowie <= 0:
            print("Gejm ołwer")
            os.system("Menu.py")
        with open(sejw, "rb") as f:
            bohater = pickle.load(f)
        print("\nJesteś obecnie w " + pokoje[obecnyPokoj]["nazwa"])
        ruch = input("> ").lower().split()
        if ruch[0] == "menu":
            os.system("Menu.py")
        if ruch[0] == "pokaz":
            bohater.show()
        if ruch[0] == "idz":
            if ruch[1] in pokoje[obecnyPokoj]:
                obecnyPokoj = pokoje[obecnyPokoj][ruch[1]]
            else:
                print("Nie mozesz tam isc")

        if ruch[0] == "zrob":
            if  pokoje[obecnyPokoj]["nazwa"] == "Latanie":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().bank()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Korytarz":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().korytarz()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                   # src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()


            if pokoje[obecnyPokoj]["nazwa"] == "Numerologia":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().numerologia()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    #src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Walka":
                if ruch[1] == "1":
                    malfoy = src.Przeciwnik.Przeciwnik("Malfoy",0,0,0)
                    malfoy.attributes()
                    walka(bohater, malfoy)
                    with open("save.obj", "wb", ) as file_hero:
                        pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL) #sejw
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().zonko()
                    src.Spotkanie.Spotkanie.dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Bank":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().bank()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

        if ruch[0] == "pomoc":               #lista
            lista = []
            print("Możesz udać się na:")
            for key, values in pokoje[obecnyPokoj].items():
                lista.append(key) #dopisuje kierunki swiata do listy
            for x in range (1,len(pokoje[obecnyPokoj])):
                print(lista[x])#wypisuje kierunki swiata w ktore moge pojsc

        if ruch[0] != "idz" and ruch[0] != "pomoc" and ruch[0] != "zrob" and ruch[0] != "wyjdz" and ruch[0] != "pokaz" :
            print("Zła komenda")
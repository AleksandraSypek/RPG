import src.Spotkanie
import pickle
import os

with open("tmp","rb") as f_temp:
    sejw = pickle.load(f_temp)

with open(sejw, "rb") as f:
    bohater = pickle.load(f)
bohater.obecnyPoziom = 1


print("Brawo, jesteś na poziomie drugim! Aby przejść dalej potrzebujesz 10 wykonanych zadań")
pokoje = {
    0 : {"nazwa" : "Królestwo", "północ" : 1, "wschód" : 2, "południe" : 3, "zachód" : 4},
    1 : {"nazwa" : "TrzyMiotły", "południe" : 0, "wschód" : 2},
    2 : {"nazwa" : "Herbaciarnia", "zachód" : 1, "południe" : 3 },
    3 : {"nazwa" : "Ulica", "północ" : 2 },
    4 : {"nazwa" : "Zonko", "wschód" : 0 }
}

obecnyPokoj = 0
print("Wybierz komendę:")
print("> idz [kierunek]")
print("> zrob - zaczyna interakcje")
print("> pomoc - wyswietla pomoc")
print("> pokaz - pokazuje statystyki gracza")
print("> menu - wychodzi do menu")
print("W każdej z lokacji możesz podać komendę \"zrob 1\" lub \"zrob 2\"")

while True:
    if bohater.wykonaneZadania > 14:
        os.system("Poziom2.py")
    else:
        if bohater.zdrowie <= 0:
            print("Gejm ołwer")
            os.system("Menu.py")
        print("Jesteś obecnie w " + pokoje[obecnyPokoj]["nazwa"])
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
            if pokoje[obecnyPokoj]["nazwa"] == "Królestwo":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().krolestwo()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "TrzyMiotły":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().miotly()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Herbaciarnia":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().herbaciarnia()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().latanie()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Ulica":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().ulica()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().korytarz()
                    src.Spotkanie.Spotkanie().dodaj()

            if pokoje[obecnyPokoj]["nazwa"] == "Zonko":
                if ruch[1] == "1":
                    src.Spotkanie.Spotkanie().zonko()
                    src.Spotkanie.Spotkanie().dodaj()
                if ruch[1] == "2":
                    src.Spotkanie.Spotkanie().herbaciarnia()
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



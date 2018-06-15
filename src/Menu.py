import os
import pickle #import bibliotek


print(""" __    __       ___      .______      .______     ____    ____    .______     ______   .___________.___________. _______ .______      
|  |  |  |     /   \     |   _  \     |   _  \    \   \  /   /    |   _  \   /  __  \  |           |           ||   ____||   _  \     
|  |__|  |    /  ^  \    |  |_)  |    |  |_)  |    \   \/   /     |  |_)  | |  |  |  | `---|  |----`---|  |----`|  |__   |  |_)  |    
|   __   |   /  /_\  \   |      /     |      /      \_    _/      |   ___/  |  |  |  |     |  |        |  |     |   __|  |      /     
|  |  |  |  /  _____  \  |  |\  \----.|  |\  \----.   |  |        |  |      |  `--'  |     |  |        |  |     |  |____ |  |\  \----.
|__|  |__| /__/     \__\ | _| `._____|| _| `._____|   |__|        | _|       \______/      |__|        |__|     |_______|| _| `._____|
                                                                                                                                      """ )
print("Witaj w grze Harry Potter i komnata programowania")
print("Wybierz akcję:")
print("[N]owa gra")
print("[W]czytaj grę")
print("[Z]akończ grę")

while True:
    char = str(input(">"))

    if char == "N":
        os.system("Intro.py")
    elif char == "Z":
        exit()
    elif char == "W":
        while True:
            iterator = 1
            print("Wybierz numer zapisu")
            for root, dirs, files in os.walk("C:/Users/sypa1/PycharmProjects/RPG/src/Saves"):
                for filename in files:
                    print(str(iterator) + ". " + filename)    #lista
                    iterator = iterator + 1
            if (iterator == 1):
                print("Brak zapisów")
                break
            else:
                zapis = int(input(">"))
                data = "Saves/"+files[zapis-1]
                with open(data, "rb") as f:          #odczyt pliku
                    postac = pickle.load(f)
                    if postac.obecnyPoziom == 1:
                        os.system("Poziom1.py")
                    if postac.obecnyPoziom == 2:
                        os.system("Poziom2.py")
                    if postac.obecnyPoziom == 3:
                        os.system("Poziom3.py")

    else:
        print("Zła komenda")
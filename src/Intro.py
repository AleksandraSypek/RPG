import random
import time
import src.Postac
import os
import pickle

class Sejw(object):
    def __init__(self, adres):
        self.adres = adres
    def ustaw(self):
        self.sejw = "Saves/" + str(self.adres)
    def wez(self):
        se = self.sejw
        return se

print("Witaj w szkole magii i czarodziejstwa. Aby rozpocząć tę niesamowitą przygodę, musisz stworzyć swojego bohatera.")
nazwa=input("\nPodaj imię twojego bohatera:\n>")
bohater = src.Postac.Bohater(nazwa, 0,0,0,0,0,1,0) #odwołuję się do drugiego pliku   #stworzenie obiekt
bohater.attributes() # losuje staty bohatera
bohater.show() #pokazuje bohatera
s = Sejw(nazwa)
s.ustaw()

with open("tmp", "wb") as f_temp:   #otwarcie pliku "tmp"
    pickle.dump(s.wez(), f_temp)    #pisanie do pliku "tmp"


print("\nWitaj ",bohater.imie, "! \nCzas wybrać twój dom. Przygotuj się na ceremonię przydziału." )

dom = random.randint(1,4)
print('Tiara już na głowie. Trafiasz do...:')
for x in range (1,4):
    print('*')
    time.sleep(1)
if dom ==  1:
    print("Gryffindor'u.")

elif dom == 2:
    print("Slytherin'u.")

elif dom == 3:
    print("Ravenclaw'u.")

elif dom == 4:
    print("Hufflepuff'u.")

print("Tiara przydziału już dobrze zdążyła Cię poznać. Wie jakie są Twoje dobre i złe strony. Czas przedstawić je także nauczycielom i znajomym, których poznasz już niedługo.")
print("Koniec intra, przechodzisz do pierwszego poziomu")
bohater.obecnyPoziom = 1

with open(s.wez(), "wb",) as file_hero:
    pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL)
text = "Loading...\n\n"
print(text)
time.sleep(3)

os.system("Poziom1.py")
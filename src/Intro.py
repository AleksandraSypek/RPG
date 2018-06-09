import random
import time
import src.Postac
import os
import pickle

print("\tJeszcze raz  witaj w szkole magii i czarodziejstwa. Aby rozpocząć tę niesamowitą przygodę, musisz stworzyć swojego bohatera.")
nazwa=input("\nPodaj imię twojego bohatera:\n>")
bohater = src.Postac.Bohater(nazwa, 0,0,0,0,0) #odwołuję się do drugiego pliku
bohater.attributes() # losuje staty bohatera
bohater.show() #pokazuje bohatera
x = bohater.show()


print("\nWitaj ",bohater.imie, "! \nCzas wybrać twój dom. Przygotuj się na ceremonię przydziału." )

dom = random.randint(1,4)
print('Tiara już na głowie. Trafiasz do...:')
for x in range (1,4):
    print('*')
   # time.sleep(1)
if dom ==  1:
    print("Gryffindor'u.")

elif dom == 2:
    print("Slytherin'u.")

elif dom == 3:
    print("Ravenclaw'u.")

elif dom == 4:
    print("Hufflepuff'u.")

print("Tiara przydziału już dobrze zdążyła Cię poznać. Wie jakie są Twoje dobre i złe strony. Czas przedstawić je także nauczycielom i znajomym, których poznasz już niedługo.")
#time.sleep(3)
print("Koniec intra, przechodzisz do pierwszego poziomu")
file_hero = open("save.obj", "wb",)
pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL)
text = "Loading...\n\n"
print(text)
#time.sleep(3)


file_hero = open("save.obj", "rb" ) #saving stats
os.system("Poziom1.py")

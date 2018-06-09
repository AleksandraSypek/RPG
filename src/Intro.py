import random
import time
import src.Postac


print("\tJeszcze raz  witaj w szkole magii i czarodziejstwa. Aby rozpocząć tę niesamowitą przygodę, musisz stworzyć swojego bohatera.")
nazwa=input("\nPodaj imię twojego bohatera:\n>")
bohater = src.Postac.Bohater(nazwa, 0,0,0,0,0) #odwołuję się do drugiego pliku
bohater.attributes() # losuje staty bohatera
bohater.show() #pokazuje bohatera

print("\nWitaj ",bohater.imie, "! \nCzas wybrać twój dom. Przygotuj się na ceremonię przydziału." )

dom = random.randint(1,4)
print('Tiara już na głowie. Trafiasz do...:')
for x in range (1,4):
    print('*')
    time.sleep(1)
if dom ==  1:
    print("\nGryffindor'u.")

elif dom == 2:
    print("\nSlytherin'u.")

elif dom == 3:
    print("\nRavenclaw'u.")

elif dom == 4:
    print("\nHufflepuff'u.")

print("Tiara przydziału już dobrze zdążyła Cię poznać. Wie jakie są Twoje dobre i złe strony. Czas przedstawić je także nauczycielom i znajomym, których poznasz już niedługo.")
print("Koniec intra, przechodzisz do kolejnego poziomu")

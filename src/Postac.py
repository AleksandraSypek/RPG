import random

class Bohater(object):
    def __init__(self, imie, inteligencja, wiedza, sila, odwaga, spryt):
        self.imie=imie
        self.inteligencja=inteligencja
        self.wiedza=wiedza
        self.sila=sila
        self.odwaga=odwaga
        self.spryt=spryt
    def attributes(self):
        self.inteligencja = random.randint(0,10)
        self.wiedza = random.randint(0, 10)
        self.sila = random.randint(0, 10)
        self.odwaga = random.randint(0, 10)
        self.spryt = random.randint(0, 10)
    def show(self):
        print('imie: ' + str(self.imie) + '\ninteligencja:' + str(self.inteligencja) + '\nwiedza: ' + str(self.wiedza) + '\nsila: ' + str(self.sila) + '\nodwaga: ' + str(self.odwaga) + '\nspryt: ' + str(self.spryt))
    def edit(self):
import random

class Bohater(object):
    def __init__(self, imie, inteligencja, wiedza, sila, odwaga, zdrowie, obecnyPoziom, wykonaneZadania):
        self.imie=imie
        self.inteligencja=inteligencja
        self.wiedza=wiedza
        self.sila=sila
        self.odwaga=odwaga
        self.zdrowie=zdrowie
        self.obecnyPoziom = obecnyPoziom
        self.wykonaneZadania = wykonaneZadania
    def attributes(self):
        self.inteligencja = random.randint(0,10)
        self.wiedza = random.randint(0, 10)
        self.sila = random.randint(0, 10)
        self.odwaga = random.randint(0, 10)
        self.zdrowie = 100
        self.obecnyPoziom = 0
        self.wykonaneZadania = 0
    def show(self):
        print('Imie: ' + str(self.imie) + '\nInteligencja: ' + str(self.inteligencja) + '\nWiedza: ' + str(self.wiedza) + '\nSila: ' + str(self.sila) + '\nOdwaga: ' + str(self.odwaga) + '\nZdrowie: ' + str(self.zdrowie) + '\nObecny poziom: ' + str(self.obecnyPoziom)+ '\nWykonane zadania: ' + str(self.wykonaneZadania))

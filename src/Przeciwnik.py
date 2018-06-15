import random

class Przeciwnik(object):
    def __init__(self, imie, sila, odwaga, zdrowie):
        self.imie=imie
        self.sila=sila
        self.odwaga=odwaga
        self.zdrowie=zdrowie
    def attributes(self):
        self.sila = random.randint(0, 10)
        self.odwaga = random.randint(0, 10)
        self.zdrowie = 100
    def show(self):
        print('Imie: ' + str(self.imie) +  '\nSila: ' + str(self.sila) + '\nOdwaga: ' + str(self.odwaga) + '\nZdrowie: ' + str(self.zdrowie))

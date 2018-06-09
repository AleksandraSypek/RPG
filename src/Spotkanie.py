import random

class Spotkanie(object):
    def __init__(self):
        print("Zaczynamy przygodę! ")
    def latanie(self):

        print("Dzień dobry wszystkim, ja to Rolanda Hooch, a wy albo przyszłe talenty i nadzieje quidditcha albo ci podający miotły, no żeby chociaż podający...Bez zbędnego gadania, wszyscy na miejsca, ustawić się koło mioteł, raz, dwa, nie ma czasu. Ręka nad miotłą wyciągnięta prosto, skupcie się, powtarzać nie będę. Wypowiadacie tylko słowa 'do mnie!', chwytacie za kij i po problemie. No nie ma ociągania. Gotowi? To zaczynamy!")
        do_mnie = input("\n\nWyciągnij rękę nad miotłę i powtórz słowa Pani profesor tak, aby miotła trafiła do twojej dłoni:\n>")

        if do_mnie == ("do mnie"):
            wywolanie = random.randint(0, 1)
            if wywolanie == 0:
                print("\n\nNo może coś z tego będzie. Pomyślimy nad testami do drużyny.")
            if wywolanie == 1:
                print(
                    "\n\nChyba musisz jeszcze troche poćwiczyć, no albo po prostu to nie dla Ciebie. Nie martw się, do kółka szachowego też kogoś na pewno szukają.")
        else:
            print("\n\nNie umiesz dwóch słów dobrze powtórzyć?! Dlaczego ja muszę pracować z takimi ludźmi...")

        print("\n\nDobra, teraz jak już wiemy w jaki sposób przywołać miotłę, a przynajmniej jakaś część z was wie, możemy przejść dalej. Siadamy na miotły. Może się nie zabijecie. Przynajmniej mam taką nadzieję, pani Pomfrey też może sobie czasem odpocząć. Okej pierwszoroczniacy, lecimy!")

        while True:
            miotla = input("\nWsiadasz na miotłę i wzbijasz się w powietrze, wpisz cyfrę, co chcesz robić dalej. 1 oznacza szybki lot przed siebie, a 2 oznacza powolne przemieszczanie się.\n>")
            if miotla == '1':
                wybor = random.randint(0, 1)
                if wybor == 0:
                    print("Oszalałeś?! Trudno, że tutaj i w taki sposób, ale mogłeś oszczędzić mi tego okropnego widoku nieudaczniku.")
                    break
                else:
                    print("Jestem w szoku! Jeśli to twój pierwszy lot na miotle, a myślę, że tak, to kapitan quidditcha Twojej drużyny na pewno usłyszy o Tobie dobre słowo. ")
                    break
            elif miotla == '2':
                wybor = random.randint(0, 1)
                if wybor == 0:
                    print("Złotego znicza byś w tym tempie nie złapał, no ale...przynajmniej sie utrzymałeś.")
                    break
                else:
                    print("Z taką prędkością wpaść w drzewo?! Moja zmarła babcia byłaby lepsza niż ty!")
                    break
            else:
                print('Zla decyzja, sprobuj jeszcze raz')
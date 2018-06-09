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
    def korytarz(self):
        print("Zwiedzasz korytarze Hogwartu i podziwiasz obrazy znanych czarodziei. Może jednak w końcu weźmiesz się do roboty")
    def numerologia(self):
        print('''Dzień dobry, witam państwa na zajęciach z numerologii. Nazywam się Septima Vector i przedstawię państwu jedną z najciekawszych technik wróżenia , przy wykorzystaniu liczb. Na początku musicie poznać państwo wartości liczbowe przypisywane danym literą. Oto one: 
        \n\n1 2 3 4 5 6 7 8 9
        A B C D E F G H I
        J K L M N O P Q R
        S T U V W X Y Z    
        \nBy zanalizować dowolne imię, trzeba zapisać imię na kartce, a pod nim cyfry przypisywane danym liczbom. Należy zsumować wszystkie cyfry. Jeśli liczba to przykładowo 50, dodajemy 5 i 0. Otrzymujemy tym samym cyfrę 5. Jeżeli suma cyfr to liczba powyżej 9 (np.14), to należy je dodawać aż do skutku (aż wyjdzie przykładowo 3).
        \n\nPierwszym Twoim zadaniem będzie odgadnięcie cyfry zsumowanej z wartości liter Nicolasa Flamela.''')

        wartosc = input("Podaj cyfrę:")
        if wartosc == ('5'):
            print(
                "\nBrawo. Piątki są zmienne, niepewne. Brak u nich stabilności i równowagi. Potrafią być energiczne, gotowe podjąć wszelkie ryzyka. Lubią podróżować, poznawać nowe rzeczy. Są również nieodpowiedzialne. Jak widać, liczby się nie mylą, cały Nicolas.")
        else:
            print(
                "\nChyba słabo jeszcze u ciebie z matematyką, ale nie przejmuj się, poćwiczymy. Teraz jednak przejdźmy dalej, szkoda czasu, tyle cyfr pozostało jeszcze nieodkrytych.")

        print("\n\nMam dla ciebie jeszcze jedno zadanie.")


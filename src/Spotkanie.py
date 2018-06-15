import random
import src.Postac
import pickle

class Spotkanie(object):
    def __init__(self):
        print("")

    def dodaj(self):
        with open("tmp", "rb") as f_temp:   #tmp przechowuje scieżkę do zapisu
            sejw = pickle.load(f_temp)
        print(sejw)
        with open(sejw, "rb") as f: #sejw przechowuje zapis
            bohater = pickle.load(f)
            bohater.wykonaneZadania = bohater.wykonaneZadania + 1
        with open(sejw, "wb", ) as file_hero:
            pickle.dump(bohater, file_hero, pickle.HIGHEST_PROTOCOL)

    def sowy(self):
        print("Dzień dobry. Witam w moim sklepie. Jesteś zainteresowany zakupem sowy? Świetnie trafiłeś! Wybierz gatunek sowy o jakim marzysz. Mam do wyboru: \n1.Sowa śnieżna \n2.Płomykówka \n3.Włochatka.")
        sowa = input("\nWybierz sowę, wpisz liczbę, która przy niej widnieje:\n>")
        kolor = input("\nTeraz wpisz kolor swojej sowy(podaj go w formie żeńskiej:\n>")
        ksywa = input("\nPodaj jeszcze imię, jakie wybrałeś sowie:\n>")

        if sowa == '1':
            print(
                "\nSuper! Właśnie stałeś się właścicielem nowego zwierzątka! Jest to" + kolor + " Sowa śnieżna, o imieniu " + ksywa)
        if sowa == '2':
            print(
                "\nSuper! Właśnie stałeś się właścicielem nowego zwierzątka! Jest to" + kolor + " Płomykówka, o imieniu " + ksywa)
        if sowa == '3':
            print(
                "\nSuper! Właśnie stałeś się właścicielem nowego zwierzątka! Jest to" + kolor + "Włochatka, o imieniu " + ksywa)
        else:
            print("\nChyba nie potrzebujesz jednak tej sowy.")

        print("\nMożesz teraz zabrać sówkę do pokoju. Dbaj o nią dobrze, to naprawde cudowne zwierzęta!")

    def olivander(self):
        print("Witaj w Sklepie Ollivanderów. Skoro mnie odwiedziłeś, to pewnie znaczy, że szukasz nowej różdżki. Cieszę się, że wybrałeś właśnie mój sklep. Chodź, zobaczymy jaka różdżka będzie dla Ciebie idealna, proszę, spróbuj tą!")
        rozdzka = random.randint(0, 1)
        if rozdzka == 0:
            print("\n*hałas spadającyh lamp*\nUps...14 cali, wierzba, róg rogatego węża. To chyba nie to czego szukamy. To nic, próbujmy dalej.")
        if rozdzka == 1:
            print("\n*hałas spadającyh lamp*\nUps...9 i pół cala, jodła, włos z ogona jednorożca. To chyba nie to czego szukamy. To nic, próbujmy dalej.")
        ideal = input("\nMoże teraz ty wybierz...Wybierasz numer 1 lub 2.\n>")
        if ideal == '1':
            print("\n*światło wokół*\nAhh...15 cali, czarny bez, włos z głowy wili. Cudownie, znaleźliśmy to, czego szukaliśmy! Ciesz się swoim nowym nabytkiem.")
        if ideal == '2':
            print("\n*światło wokół*\nAhh...8 i 3/4 cala, wiśnia, pióro z ogona gromoptaka. Cudownie, znaleźliśmy to, czego szukaliśmy! Ciesz się swoim nowym nabytkiem.")
        else:
            print("\nNie wybierzesz sam? No trudno, może innym razem.")

        print("Może zobaczmy czy na pewno dobrze działa. Spróbuj jakiegoś prostego ruchu.")
        ruch = input("Wpisz komendę, w jaki sposób chcesz wykonać ruch, masz do wyboru 'prosto' lub 'obrot'\n>")
        if ruch == "prosto":
            print("\nIdealnie podnosisz przedmioty, widzę, że nauka zaklęć idzie Ci całkiem nieźle!")
        elif ruch == "obrot":
            print("\nWybuchanie niektórych rzeczy też czasem się przydaje, naprawdę, nawet częściej niż myślisz!")
        else:
            print("Pole, pole. Łyse pole")

    def quiditch(self):
        print("Witaj młody zawodniku quidditcha. Potrzebujesz nowego sprzętu? Dobrze, że tu jesteś! Zaraz znajdziemy to, czego szukasz.")
        sprzet = input("Powiedz czego potrzebujesz? To, co masz do wyboru to miotła, piłka, strój. Wpisuj dokładnie!\n>")
        if sprzet == 'miotła':
            print("\nŚwietnie, mam dla ciebie Nimbusa 2000! Myślę, że będziesz zadowolony.")
        elif sprzet == 'piłka':
            print("\nnMam cały zestaw. Będzie on pewnie przydatny w nauce. Znajduje się w nim tłuczek, kafel i złoty znicz")
        elif sprzet == 'strój':
            print("\nAhh, w tym czarnym kombinezonie będziesz prezentował się wspaniale!")
        else:
            print("Zrezygnowałeś? Trudno, sklepu nie zamykamy, może później się zdecydujesz.")

        print("Słuchaj, siedzimy na zapleczu z byłym zawodnikiem Harpii z Holyhead. Chcesz wpaść pogadać?")
        odpo = input("Odpowiedz tak lub nie.\n.")
        if odpo == 'tak':
            print("Świetnie! Chodź, na pewno dowiesz się sporo ciekawych rzeczy na temat quidditcha!")
        if odpo == 'nie':
            print("Nie masz czasu ani ochoty? Szkoda, żałuj, taka okazja może się nie powtórzyć.")
        else:
            print("Skoro jesteś niezdecydowany, trudno, twoja strata.")

    def kociol(self):
        print("Witaj w Dziurawym Kotle! Siadaj słoneczko w naszym pięknym lokalu! Proszę, oto 3 napoje, które dzisiaj dostaniesz: \n1.Napój pomarańczowy \n2.Napój niebieski \n3.Napój różowy")
        napoj = str(input("\nWybierz numer zamówienia i wpisz:\n>"))
        if napoj == '1':
            print("\nDobry wybór. Pomarańcza i drobny dodatek, idealne połączenie!")
        if napoj == '2':
            print("\nDobry wybór. Jagoda i drobny dodatek, idealne połączenie!")
        if napoj == '3':
            print("\nDobry wybór. Malina i drobny dodatek, idealne połączenie!")
        else:
            print("\nNie możesz się zdecydować, żałuj, najlepsze soki tylko u nas")

        print("\nChcesz zostać jeszcze na noc w naszym pokoju? Świetnie! Zaraz poszukamy pokoju.")
        pokoj = input("\nWolisz piętro 3 czy 4? Wpisz cyfrę:\n>")
        if pokoj == '3':
            print("\nTwoją sąsiadką będzie stara samotna wiedźma, czasem krzyczy po nocach, ale raczej jest nieszkodliwa, nie martw się")
        if pokoj == '4':
            print("\nTwoją sąsiadką będzie Twój rówieśnik. Wydaje się podejrzany, ale może akurat okarze się dobrym kolegą")
        else:
            print("To jest kurwa dramat. Że w tym antyludzkim państwie...")

    def krolestwo(self):
        print("Witaj w Miodowym królestwie, najsłodszym miejscu w całym Hogsmeade. Zapraszamy w podróż pełną rozkoszy. Smakołyków u nas nigdy Ci nie zabraknie! Proponuję jednak rozpocząć od fasolek wszystkich smaków. Mamy do wyboru:\n1.różową \n2.zieloną \n3.niebieską.")
        while True:
            fasolka = str(input("\nWybierz, którą fasolkę wybierasz, wpisz cyfrę:\n>"))
            if fasolka == '1':
                print("\nZjadłeś fasolkę łososiową. Mogło być gorzej.")
                break
            if fasolka == '2':
                print("\nZjadłeś fasolkę goblinową. Szczerze współczuję.")
                break
            if fasolka == '3':
                print("\nZjadłeś fasolkę o smaku kandyzowanych fiołków. Dziwne, ale nie najgorsze.")
                break
            else:
                print("\nZła liczba")

        print("\nKoniec kosztowania. Masz teraz szansę na gratisową paczkę słodyczy. Pomyśl liczbę od 1-5.")
        paczka = input("Podaj liczbę:\n>")
        if paczka == '1':
            print("\nWylosowałeś Kremowe Bryły Nugatu")
        if paczka == '2':
            print("\nWylosowałeś Różowe kostki lodów kokosowych")
        if paczka == '3':
            print("\nWylosowałeś Kociołkowe pieguski")
        if paczka == '4':
            print("\nWylosowałeś Lukrecjowe różdżki")
        if paczka == '5':
            print("\nWylosowałeś Szkieletowe słodycze")
        else:
            print("\nPrzykro mi, nic nie dostaniesz")

    def miotly(self):
        print("Witam kochanie w Trzech Miotłach. Siadaj, zaraz przyniosę Ci kremowe piwo. Mogę posiadzić kogoś koło Ciebie?")
        gosc = input("\nChcesz, aby ktoś się przysiadł?\n>")
        if gosc == 'nie':
            print("\nSzkoda, ten gość naprawdę mógł Ci powiedzieć wiele ciekawych rzeczy.")
        if gosc == 'tak':
            print(
                "\nŚwietnie, myślę, że się dogadacie, jest to były profesor, a przy okazji, tak między nami, dobry znajomy ministrów, takie znajomości na pewno się przydadzą.")
        else:
            print("\nNie wiesz? To nic, zaprowadzę go gdzie indziej.")

    def zonko(self):
        print("Witamy w  królestwie żartobliwych niespodzianek i najśmieszniejszych psikusów! Zachęcamy do obejrzenia całego naszego asortymentu. Jednak to, co mogę ci polecić to łajnobomby. Na pewno jest już w szkole ktoś, kogo nie obdarzyłeś sympatią")
        lajno = random.randint(1, 3)
        if lajno == 1:
            print("\nWziąłeś łajnobomby, jednak pękły Ci w rękach i ewakuujesz cały sklep, tragedia")
        elif lajno == 2:
            print("\nPodrzucasz łajnobomby do torby przypadkowej osobie w sklpie. Niezła zabawa")
        else:
            print("Bedom cycki bedzie pompa. Skresl to. Hihihi haha")

    def ulica(self):
        print("Znajdujesz się na głównej ulicy Hogsmeade. Podchodzi do Ciebie dwójka chłopaków. Zaczynasz rozmowę czy odchodzisz?")
        ulica = input("Wpisz komendę rozmowa lub odejscie\n>")
        if ulica == 'rozmowa':
            print("\nCześć, szukamy osób do nowego stowarzyszenia, które promuje walkę z Sam Wiesz Kim, chcesz wpaść na spotkanie?")
            stowarzyszenie = input("\nWpisz tak lub nie:\n>")
            if stowarzyszenie == 'nie':
                print("\nSzkoda, fajnie byłoby mieć taką osobę w drużynie.")
            if stowarzyszenie == 'tak':
                print(
                    "\nSuper! Chodź z nami, pokażemy Ci wszystko i przedstawimy resztę członków. Wolisz iść na spotkanie organizacyjne czy odrazu rozpocząć naukę czarów?")
                wolisz = input("\nWpisz komendę spotkanie lub nauka:\n>")
                if wolisz == 'spotkanie':
                    print("\nOkej, poznamy Cię z głównodowodzącym, opowie ci o idei naszego stowarzyszenia.")
                if wolisz == 'nauka':
                    print("\nOkej, przejdziemy odrazu do machania różdżką, podoba mi się Twoje szybkie zaangażowanie.")
        if ulica == 'odejscie':
            print("\nIdziesz dalej zwiedzać Hogsmeade.")

    def herbaciarnia(self):
        print("Wiatj w Herbaciarni u pani Puddifoot. Widzę, że dziś nie przyszedłeś sam. Jak ma na imię twój znajomy?")
        znajomy = input("\nPodaj imię swojego znajomego:\n>")
        print("\nWitaj " + str(znajomy) + "! Miło zobaczyć tu w końcu nową twarz. Może poza herbatą macie ochote na moje nowe ciasteczka?")
        ciastko = input("\nChcesz zjeść ciastko?\n>")
        if ciastko == 'nie':
            print("\nŻałujcie, wyszły mi naprawdę przepyszne!")
        if ciastko == 'tak':
            print("\nJak miło, a jakie wolicie, czekoladowe czy waniliowe?")
            czekwan = input("Które ciastko wolisz?\n>")
            if czekwan == 'czekoladowe':
                print("\nŚwietnie, robione z najlepszej czekolady w okolicy.")
            if czekwan == 'waniliowe':
                print("\nŚwietnie, sama dbam o dostawy najlepszej wanilii.")
            else:
                print("\nNie możesz się zdecydować? Trudno, sama coś wybiorę.")
        else:
            print("\nAhh, sam nie wiesz czego chcesz.")

    def bank(self):
        # bank
        print("Witaj w Banku Gringotta. Zapewne chciałbyś dostać się do swoich pieniędzy. Widzę, że nie masz pojęcia jaki jest numer Twojej skrytki. No cóż, ja Ci nie pomogę, chyba musisz zgadnąć go sam. \n\nPowiem Ci, ze twoja skrytna mieści między liczbami 100 a 200.")

        kod = random.randint(100,200)
        print("Zgadnij skrytkę: ")
        print(kod)
        typ = int(input(">"))

        while True:
            if type(typ) != int:
                print("Podaj liczbę debilu")
                typ = int(input(">"))
            elif type(typ) == int:
                if typ != kod:
                    if typ > kod:
                        print("Za dużo, podaj mniejszą liczbę.")
                        typ = int(input(">"))
                    elif typ < kod:
                        print("Za mało, podaj większą liczbę.")
                        typ = int(input(">"))
                elif typ == kod:
                    print("Brawo, zgadłeś")
                    break

        while True:
            stan = 2567
            strStan = str(stan)
            print("Twój stan konta to: " + strStan)
            print("Ile chcesz wypłacić?")
            wyplata = int(input(">"))
            if wyplata > stan:
                print("Nie masz tyle na koncie.")
            else:
                stan = stan - wyplata
                print("Masz obecnie " + str(stan) + " hajsu.")
                break


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
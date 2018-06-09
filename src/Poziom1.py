import src.Spotkanie


print('Znajdujesz się na poziomie 1. Możesz udać się na pólnoc, wschod zachod lub poludnie')
rooms = {
    0 : {"name" : "Korytarz", "north" : 1, "east" : 2, "south" : 3, "west" : 4},
    1 : {"name" : 'Latanie', "south" : 0} # itd tu uzupełinasz według schematu który Ci wyślę i uzupełniasz nazwy pokoi
}

currentRoom = 0
print("Wybierz komendę:")
print("> go [direction]")
print(">zrob - zaczyna interakcje")
print((">help - wyswietl pomoc"))
print("> exit - exiting the game")

while True:
    print("Jesteś obecnie w " + rooms[currentRoom]["name"])
    move = input("> ").lower().split()
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == "zrob":
        if  rooms[currentRoom]["name"] == "Latanie":
            src.Spotkanie.Spotkanie().latanie()
        if rooms[currentRoom]["name"] == "Korytarz":
            src.Spotkanie.Spotkanie().korytarz()

    if move[0] == "help":
        lista = []
        print("Możesz udać się na:")
        for key, values in rooms[currentRoom].items():
            lista.append(key) #dopisuje kierunki swiata do listy
        for x in range (1,len(rooms[currentRoom])):
            print(lista[x])#wypisuje kierunki swiata w ktore moge pojsc

    if move[0] == "exit":
        print("You exit the game!")
        break
    if move[0] != "go" and move[0] != "help" and move[0] != "zrob" and move[0] != "exit":
        print("Zła komenda")



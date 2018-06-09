import src.Spotkanie


print('Znajdujesz się na poziomie 1. Możesz udać się na pólnoc, wschod zachod lub poludnie')
rooms = {
    0 : {"name" : 'Pokoj0', "north" : 1, "east" : 2, "south" : 3, "west" : 4},
    1 : {"name" : 'Latanie', "south" : 0} # itd tu uzupełinasz według schematu który Ci wyślę i uzupełniasz nazwy pokoi
}

currentRoom = 0
print("Wybierz komendę:")
print("> go [direction]")
print(">zrob - zaczyna interakcje")
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
    if move[0] == "exit":
        print("You exit the game!")
        break



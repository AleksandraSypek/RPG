import sys
import os

print(""" __    __       ___      .______      .______     ____    ____    .______     ______   .___________.___________. _______ .______      
|  |  |  |     /   \     |   _  \     |   _  \    \   \  /   /    |   _  \   /  __  \  |           |           ||   ____||   _  \     
|  |__|  |    /  ^  \    |  |_)  |    |  |_)  |    \   \/   /     |  |_)  | |  |  |  | `---|  |----`---|  |----`|  |__   |  |_)  |    
|   __   |   /  /_\  \   |      /     |      /      \_    _/      |   ___/  |  |  |  |     |  |        |  |     |   __|  |      /     
|  |  |  |  /  _____  \  |  |\  \----.|  |\  \----.   |  |        |  |      |  `--'  |     |  |        |  |     |  |____ |  |\  \----.
|__|  |__| /__/     \__\ | _| `._____|| _| `._____|   |__|        | _|       \______/      |__|        |__|     |_______|| _| `._____|
                                                                                                                                      """ )
print("Witaj w grze Harry Potter i komnata spierdolenia")
print("Wybierz akcję:")
print("[N]owa gra")
print("[W]czytaj grę")
print("[Z]akończ grę")
char = input()

if char == "N":
    os.system("Intro.py")
elif char == "W":
    print("wczytujemy")
    #Wczytujemy gre
elif char == "Z":
    sys.exit
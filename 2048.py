import random
from tools import *
import keyboard

# grille
def init_grid() -> list[list[int]]:
    grid: list[list[int]] = []
    
    for i in range(0,4):
        line = []
        for j in range(0,4):
            line.append(0)
        grid.append(line)

    return grid
    #return [[0 for _ in range(4)] for _ in range(4)]

# Fonction pour ajouter un nombre aléatoire (2 ou 4) à un emplacement vide
def add_new(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = generate()

# Fonction pour afficher la grille
def Afficher_grid(grid: list[list[int]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if not j == len(grid) - 1:  # pour ne pas avoir de "|" à la fin
                if grid[i][j] == 0:  # pour avoir un bel affichage
                    print(" ", end="    | ")
                elif grid[i][j] < 10:
                    print(grid[i][j], end="    | ")
                elif grid[i][j] < 100:
                    print(grid[i][j], end="   | ")
                elif grid[i][j] < 1000:
                    print(grid[i][j], end="  | ")
                elif grid[i][j] < 10000:
                    print(grid[i][j], end=" | ")
                else:
                    print(grid[i][j], end="| ")
            else:
                if not grid[i][j] == 0:
                    print(grid[i][j])
                else:
                    print(" ")


# fonction pour generer un nombre aleatoire dans la grille avec proba
def generate():
    rand = random.randint(1,10)
    if rand < 9:
        return 2
    else:
        return 4
    


#mouv a droite
def move_right(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])-1, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
        for i in range(len(grid)):
            grid[i].sort(key=lambda x: 1 if x == 0 else 0, reverse=True)

#mouv a gauche
def move_left(grid):
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid)):
                if grid[i][j-1] == 0:
                    grid[i][j] = grid[i][j-1]
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if grid[i][j] == grid[i][j-1] and grid[i][j] != 0:
                grid[i][j - 1] *= 2
                grid[i][j] = 0 
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid)):
                if grid[i][j-1] == 0:
                    grid[i][j] = grid[i][j-1]

#mouv en haut
def move_up(grid):
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid[i])):
                if grid[j - 1][i] == 0:
                    grid[j][i], grid[j - 1][i] = grid[j - 1][i], grid[j][i]
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if grid[j][i] == grid[j - 1][i] and grid[j][i] != 0:
                grid[j - 1][i] *= 2
                grid[j][i] = 0 
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid[i])):
                if grid[j - 1][i] == 0:
                    grid[j][i], grid[j - 1][i] = grid[j - 1][i], grid[j][i]      

#mouv en bas
def move_down(grid):
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(len(grid) - 2, -1, -1):
                if grid[j + 1][i] == 0:
                    grid[j + 1][i], grid[j][i] = grid[j][i], grid[j + 1][i]

    for i in range(len(grid)):
        for j in range(len(grid) - 2, -1, -1):
            if grid[j][i] == grid[j + 1][i] and grid[j][i] != 0:
                grid[j + 1][i] *= 2
                grid[j][i] = 0
    for i in range(len(grid)):
        for _ in range(len(grid) - 1):
            for j in range(len(grid) - 2, -1, -1):
                if grid[j + 1][i] == 0:
                    grid[j + 1][i], grid[j][i] = grid[j][i], grid[j + 1][i]


def victoras(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells == []:
        for i in range(1, len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == grid[i-1][j]:
                    return False
                elif grid[j][i] == grid[j][i-1]:
                    return False
                elif grid[i][j] == 2048:
                    print("vous avez gagner")
                    return True
        print("vous avez perdu bande de merde")
        return True



def game():
    

    grid = init_grid()
    add_new(grid)
    Afficher_grid(grid)
    print("\n")
    generate()     
    
   
    while True:
        event = keyboard.read_event()
        if keyboard.is_pressed('up'):
            move_up(grid)
            add_new(grid)
            Afficher_grid(grid)
            print("\n")
            if victoras(grid):
                break
        if keyboard.is_pressed('down'):
            move_down(grid)
            add_new(grid)
            Afficher_grid(grid)
            print("\n")
            if victoras(grid):
                break
        if keyboard.is_pressed('right'):
            move_right(grid)
            add_new(grid)
            Afficher_grid(grid)
            print("\n")
            if victoras(grid):
                break
        if keyboard.is_pressed('left'):
            move_left(grid)
            add_new(grid)
            Afficher_grid(grid)
            print("\n")
            if victoras(grid):
                break


def regame():
    v =  AskInput("voulez vous rejouer? (oui/non) ",["oui","non"])
    if v == 'oui':
        param()
    else:
        print("au revoir")


def param():
    
        yes = AskInput("bienvenue dans le jeux du 2048 pour commencer ecriver oui sinon ecriver non ",["oui","non"])
        if yes == "oui":
            print("go")
            game()
            regame()
        else:
            print("au revoir")

#param()

grid1 = [
    [0,0,0,0],
    [2,2,2,2],
    [0,0,0,0],
    [2,0,0,2],
]

move_left(grid1)
print(grid1)
grid2 = [
    [0,0,0,0],
    [4,4,0,0],
    [0,0,0,0],
    [4,0,0,0],
]

print(grid1 == grid2)



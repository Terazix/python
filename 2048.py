import random
from tools import *
import keyboard

# grille
def init_grid():
    return [[0 for _ in range(4)] for _ in range(4)]

# Fonction pour ajouter un nombre aléatoire (2 ou 4) à un emplacement vide
def add_new(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = generate()

# Fonction pour afficher la grille
def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) if cell != 0 else '-' for cell in row))
    print()

# fonction pour generer un nombre aleatoire dans la grille avec proba
def generate():
    rand = random.randint(1,10)
    if rand < 9:
        return 2
    else:
        return 4
    



def move_right(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])-1, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
    for i in range(len(grid)):
        grid[i].sort(key=lambda x: 1 if x == 0 else 0, reverse=True)


def move_left(grid):
    for i in range (len(grid)-1):
        for j in range(len(grid)-1):
             if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
    for i in range(len(grid)):
        grid[i].sort(key=lambda x: 1 if x == 0 else 0)


def move_up(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])-1):
            if grid[j][i] == grid[j][i - 1] and grid[j][i] != 0:
                grid[j][i] *= 2
                grid[j][i - 1] = 0
    for j in range(len(grid)):
        grid[j].sort(key=lambda x: 1 if x == 0 else 0, reverse=True)


def move_down(grid):
    for i in range (len(grid)-1):
        for j in range(len(grid)-1,0,-1):
             if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
    for i in range(len(grid)):
        grid[i].sort(key=lambda x: 1 if x == 0 else 0)

def game():
    

    grid = init_grid()
    add_new(grid)
    print_grid(grid)
    generate()     
    
   
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "haut":
            #move_up(grid)
            add_new(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "bas":
            #move_down(grid)
            add_new(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "droite":
            move_right(grid)
            add_new(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "gauche":
            move_left(grid)
            add_new(grid)
            print_grid(grid)

def param():
    
        yes = AskInput("bienvenue dans le jeux du 2048 pour commencer ecriver oui sinon ecriver non ",["oui","non"])
        if yes == "oui":
            print("go")
            game()
        else:
            print("au revoir")

param()






import random
from tools import *
import keyboard

# grille
def init_grid():
    return [[0 for _ in range(4)] for _ in range(4)]

# Fonction pour ajouter un nombre aléatoire (2 ou 4) à un emplacement vide
def add_new(grid):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0]
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
    rand = random.randint(1,100)
    if rand < 90:
        return 2
    else:
        return 4
    



def move_left(grid):
    for i in range (len(grid)-1):
        for j in range(len(grid)-1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    grid.sort(key=lambda x: 1 if x == 0 else 0)


def move_right(grid):
    for row in grid:
        for i in range (len(grid)-1):
            for j in range(len(grid)-1):
                if row[j] == row[j - 1] and row[j] != 0:
                    row[j] *= 2
                    row[j - 1] = 0
        row.sort(key=lambda x: 1 if x == 0 else 0)


def move_up(grid):
    for row in grid:
        for i in range(len(grid)-1):
            for j in range(len(grid)-1):
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] *= 2
                    row[i + 1] = 0
        row.sort(key=lambda x: 1 if x == 0 else 0)

def move_down(grid):
    for row in grid:
        for i in range(len(grid)-1):
            for j in range(len(grid)-1):
                if row[i] == row[i - 1] and row[i] != 0:
                    row[i] *= 2
                    row[i - 1] = 0
        row.sort(key=lambda x: 1 if x == 0 else 0)


def game():
    
    AskInput("bienvenue dans le jeux du 2048 pour commencer ecriver oui sinon ecriver non",["oui","non"])
    if AskInput == "oui":
        print("go")
    else:
        print("au revoir") 
       
    grid = init_grid()
    v = len(grid) 
    add_new(grid)
    print_grid(grid)
    generate()     
    
   
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "haut":
            move_up(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "bas":
            move_down(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "droite":
            move_left(grid)
            print_grid(grid)
        if event.event_type == keyboard.KEY_DOWN and event.name == "gauche":
            move_right(grid)
            print_grid(grid)
          
game()




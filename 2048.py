import random
import keyboard
from tools import *


# grille
def init_grid():
    return [[0 for _ in range(3)] for _ in range(3)]

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
    for row in grid:
        for i in range(3):
            for j in range(3):
                if row[j] == row[j + 1] and row[j] != 0:
                    row[j] *= 2
                    row[j + 1] = 0
        row.sort(key=lambda x: 1 if x == 0 else 0)

# fonction jeux
def game():
    
    print("bienvenue dans le jeux du 2048 pour commencer ecriver oui sinon ecriver non")
    AskInput(["oui","non"])
    if AskInput == "oui":
        print("go")
    else:
        print("au revoir") 
        
    grid = init_grid()
    add_new(grid)
    print_grid(grid)
    generate()     
    
    while True:
        move = input("taper sur une fleche")
        if move == 'left':
            move_left(grid)
        elif move == 'right':
            move_right(grid)
        elif move == 'up':
            move_up(grid)
        elif move == 'down':
            move_down(grid)
        else: 
            print("veuille appuyer sur une des fleche") 
        add_new(grid)
        print_grid(grid)      
        
                
game()


import random
from tools import *
import keyboard
gameRunning: bool = True
testRunning: bool = False


# grille
def init_grid() -> list[list[int]]:
    grid: list[list[int]] = []
    for i in range(0, 4):
        line: list = []
        for j in range(0, 4):
            line.append(0)
        grid.append(line)
    return grid
   


# Fonction pour ajouter un nombre aléatoire (2 ou 4) à un emplacement vide
def add_new(grid) -> None:
    empty_cells: list[tuple[int, int]] = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
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
def generate() -> int:
    rand: int = random.randint(1, 10)
    if rand < 9:
        return 2
    else:
        return 4


def move_right(grid: list[list[int]], score: int) -> int:
    for i in range(len(grid)):
        # Déplacement de tout les éléments vers la droite
        for _ in range(len(grid[i]) - 1):
            for j in range(len(grid[i]) - 1, 0, -1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j - 1]
                    grid[i][j - 1] = 0
        # Fusion des éléments identiques
        for j in range(len(grid[i]) - 1, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                score += grid[i][j]
                grid[i][j - 1] = 0
        # Déplacement de tout les éléments vers la droite une seconde fois
        for _ in range(len(grid[i]) - 1):
            for j in range(len(grid[i]) - 1, 0, -1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j - 1]
                    grid[i][j - 1] = 0
    return score


def move_left(grid: list[list[int]], score: int) -> int:
    for i in range(len(grid)):
        # Déplacement de tout les éléments vers la gauche
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid[i])):
                if grid[i][j - 1] == 0:
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j] = 0
        # Fusion des éléments identiques
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                score += grid[i][j]
                grid[i][j + 1] = 0
        # Déplacement de tout les éléments vers la gauche une seconde fois
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid[i])):
                if grid[i][j - 1] == 0:
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j] = 0
    return score


def move_up(grid: list[list[int]], score: int) -> int:
    for i in range(len(grid)):
        # Déplacement de tout les éléments vers le haut
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid)):
                if grid[j - 1][i] == 0:
                    grid[j][i], grid[j - 1][i] = grid[j - 1][i], grid[j][i]
        # Fusion des éléments identiques
        for j in range(1, len(grid[i])):
            if grid[j][i] == grid[j - 1][i] and grid[j][i] != 0:
                grid[j - 1][i] *= 2
                score += grid[j - 1][i]
                grid[j][i] = 0
        # Déplacement de tout les éléments vers le haut une seconde fois
        for _ in range(len(grid) - 1):
            for j in range(1, len(grid)):
                if grid[j - 1][i] == 0:
                    grid[j][i], grid[j - 1][i] = grid[j - 1][i], grid[j][i]
    return score


def move_down(grid: list[list[int]], score: int) -> int:
    for i in range(len(grid)):
        # Déplacement de tout les éléments vers le bas
        for _ in range(len(grid) - 1):
            for j in range(len(grid) - 2, -1, -1):
                if grid[j + 1][i] == 0:
                    grid[j + 1][i], grid[j][i] = grid[j][i], grid[j + 1][i]
        # Fusion des éléments identiques
        for j in range(len(grid) - 2, -1, -1):
            if grid[j][i] == grid[j + 1][i] and grid[j][i] != 0:
                grid[j + 1][i] *= 2
                score += grid[j + 1][i]
                grid[j][i] = 0
        # Déplacement de tout les éléments vers le bas une seconde fois
        for _ in range(len(grid) - 1):
            for j in range(len(grid) - 2, -1, -1):
                if grid[j + 1][i] == 0:
                    grid[j + 1][i], grid[j][i] = grid[j][i], grid[j + 1][i]
    return score


def victoras(grid: list[list[int]]) -> bool:
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if not empty_cells:
        for i in range(1, len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 2048 or grid[i - 1][j] == 2048:
                    print("Vous avez gagner")
                    return True
                elif grid[i][j] == grid[i - 1][j]:
                    return False
                elif grid[j][i] == grid[j][i - 1]:
                    return False
        print("Vous avez perdu")
        return True


def game() -> None:
    grid: list[list[int]] = init_grid()
    score: int = 0
    add_new(grid)
    add_new(grid)
    Afficher_grid(grid)
    print("Score :", score)
    print("\n")
    generate()
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "haut":
            score = move_up(grid, score)
            add_new(grid)
            Afficher_grid(grid)
            print("Score :", score, "\n")
            if victoras(grid):
                break
        if event.event_type == keyboard.KEY_DOWN and event.name == "bas":
            score = move_down(grid, score)
            add_new(grid)
            Afficher_grid(grid)
            print("Score :", score, "\n")
            if victoras(grid):
                break
        if event.event_type == keyboard.KEY_DOWN and event.name == "droite":
            score = move_right(grid, score)
            add_new(grid)
            Afficher_grid(grid)
            print("Score :", score, "\n")
            if victoras(grid):
                break
        if event.event_type == keyboard.KEY_DOWN and event.name == "gauche":
            score = move_left(grid, score)
            add_new(grid)
            Afficher_grid(grid)
            print("Score :", score, "\n")
            if victoras(grid):
                break


while gameRunning:
    print("2048 Use the arrow keys\n")
    game()
    if AskInput("Do you want to restart\n", ["YES", "NO"]) == "NO":
        gameRunning = False

if testRunning:
    grid1 = [
        [0, 0, 0, 0],
        [2, 2, 2, 2],
        [0, 0, 0, 0],
        [2, 0, 0, 2],
    ]
    move_right(grid1, 0)
    grid2 = [
        [0, 0, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 4],
    ]
    print("test move_right", grid1 == grid2)

    grid1 = [
        [0, 0, 0, 0],
        [2, 2, 2, 2],
        [0, 0, 0, 0],
        [2, 0, 0, 2],
    ]
    move_left(grid1, 0)
    grid2 = [
        [0, 0, 0, 0],
        [4, 4, 0, 0],
        [0, 0, 0, 0],
        [4, 0, 0, 0],
    ]
    print("test move_left", grid1 == grid2)

    grid1 = [
        [2, 0, 0, 2],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 2],
    ]
    move_up(grid1, 0)
    grid2 = [
        [4, 0, 0, 4],
        [4, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    print("test move_up", grid1 == grid2)

    grid1 = [
        [2, 0, 0, 2],
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 0, 0, 2],
    ]
    move_down(grid1, 0)
    grid2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 0, 0, 0],
        [4, 0, 0, 4],
    ]
    print("test move_down", grid1 == grid2)

    grid1 = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    print("Test victoras avec 0 mouvement possible", victoras(grid1))

    grid1 = [
        [2, 4, 2, 4],
        [4, 2, 0, 2],
        [2, 0, 2, 4],
        [4, 2, 4, 2],
    ]
    print("Test victoras avec case vide", victoras(grid1))

    grid1 = [
        [1024, 1024, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    grid2 = [
        [2048, 1024, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]
    print("Test victoras avec mouvement possible", victoras(grid1))
    move_left(grid1, 0)
    print("Test victoras avec 2048", victoras(grid2))

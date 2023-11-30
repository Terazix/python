import random
from tools import *
def showcase(field):
    for i in range(len(field)):
        if i % 3 == 0:
            print('\n')
        print(field[i], end=" ")
    print('\n')

#faire avec 2 boucle for
def check_winner(field):
    for i in range(3):
        if field[i * 3] == field[i * 3 + 1] == field[i * 3 + 2] != '.':
            return field[i * 3]
        if field[i] == field[i + 3] == field[i + 6] != '.':
            return field[i]
    for i in range(0, 3, 2):
        if field[i] == field[4] == field[8 - i] != '.':
            return field[i]
    
    return None


#fonction avec un tableau case vide
#verifier chaque case vide
#ajouter les cae libre au tableau et le faire random entre les case libre
def check_field(field):

    empty: list = []
    while True:

        for field in range(len(field)):
            if  != 'X' or 'O':
                empty.append(field)
            return empty
        
        
        




def game():
    field = [".", ".", ".", ".", ".", ".", ".", ".", "."]

    while True:
        #PLAYER 
        user = AskInt("Choisissez un nombre entre 0 et 8: ")

        if field[user] != '.':
            print("Cette case est déjà prise. Veuillez choisir une autre case.")
            continue

        field[user] = "X"
       
        #COMPUTER
        # a ameliorer
        
        a = check_field(field)
        computer = random.randint(0,len(a))
        
        field[computer] = "O"
        
        showcase(field)

        winner = check_winner(field)
        if winner:
            print(f"Le joueur {winner} a gagné!")
            break
game()

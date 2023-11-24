import random
from tools import * 

def start(essais,max_essais,nombre,min,max):
    
    while essais < max_essais:
            essai: int = AskInt(f"Devinez le nombre entre {min} et {max} : ")
            essais += 1
            if essai < nombre:
                print("C'est plus !")
            elif essai > nombre:
                print("C'est moins !")
            elif essai == nombre:
                print(f"Félicitations ! Vous avez trouvé le nombre mystère ({nombre}) en {essais} essais")
                break   
            elif essais == max_essais:
                print(f"Dommage ! Vous avez dépassé le nombre maximal d'essais. Le nombre mystère était {nombre}")
                break


def game():
    print("Bienvenue dans le jeu Devine le Nombre !")
    while True:
        borne: str = AskInput("Voulez-vous définir des bornes personnalisées ? (oui/non) : ",["oui","non"])
        if  borne == "oui":
            min: int = AskInt("Entrez la borne minimale : ")
            max:int  = AskInt("Entrez la borne maximale : ")
        else:
            min, max = 1, 100
        
        nombre: int = random.randint(min, max)
        print(nombre)
        essais: int = 0
        max_essais: int = 10
        start(essais,max_essais,nombre,min,max)
        rejouer: str = AskInput("Voulez-vous jouer à nouveau ? (oui/non) : ",["non","oui"])
        if rejouer == "oui":
            print("go") 
        else: 
            break
game()
       


           










import random

def AskInt(message: str) -> int: 
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("entre un truc valide")

def AskInput(message: str, choice: list[str]) -> str:
    while True:
        user_in = input(message)

        if user_in in choice:
            return user_in

        print("champs non valide")
        print("veuiller reessayer")

        
            


def start(essais,max_essais,nombre,min,max):
    
    while essais < max_essais:
            essai = AskInt(f"Devinez le nombre entre {min} et {max} : ")
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
        borne = AskInput("Voulez-vous définir des bornes personnalisées ? (oui/non) : ",["oui","non"])
        if  borne == "oui":
            min = AskInt("Entrez la borne minimale : ")
            max = AskInt("Entrez la borne maximale : ")
        else:
            min, max = 1, 100
        
        nombre = random.randint(min, max)
        print(nombre)
        essais = 0
        max_essais = 10
        start(essais,max_essais,nombre,min,max)
        rejouer = AskInput("Voulez-vous jouer à nouveau ? (oui/non) : ",["non","oui"])
        if rejouer == "oui":
            print("go") 
        else: 
            break
game()
       


           










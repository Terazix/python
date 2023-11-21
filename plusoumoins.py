import random

def AskInt() -> int: 
    while True:
        try:
            user_input = int(input(""))
            return user_input
        except ValueError:
            print("entre un truc valide")
      
def plusmoin():
    print("Bienvenue dans le jeu Devine le Nombre !")
    while True:
        borne = input("Voulez-vous définir des bornes personnalisées ? (oui/non) : ")
        
        if  borne == "oui":
            min = input("Entrez la borne minimale : ")
            AskInt()
            max = input("Entrez la borne maximale : ")
            AskInt()
        else:
            min, max = 1, 100
        
        nombre = random.randint(min, max)
        essais = 0
        max_essais = 10
        
        while essais < max_essais:
            essai = input(f"Devinez le nombre entre {min} et {max} : ")
            AskInt()
            essais += 1

            if essai == nombre:
                print(f"Félicitations ! Vous avez trouvé le nombre mystère ({nombre}) en {essais} essais")
                
            elif essai < nombre:
                print("C'est plus !")
            else:
                print("C'est moins !")
            break
        else:
            print(f"Dommage ! Vous avez dépassé le nombre maximal d'essais. Le nombre mystère était {nombre}")
        rejouer = input("Voulez-vous jouer à nouveau ? (oui/non) : ")
        if rejouer != "oui":
            print("Merci d'avoir joué ! Au revoir.")
        break
 
plusmoin()

           










import random

def restart(): 
    print("vouler vous recommencer?")
    rep = str(input("dite oui ou non"))
    
    if rep == str("oui"):
        jeux()
    else:
        print("gg")
        



def jeux():
    print("bienvenue dans le plus ou moins")
    nombre: int = random.randint(1,100)
    essai: int = 10
    while essai > 0:

        nb_user = int(input("deviner le nombre choisit par l'IA "))
         
        essai = essai-1
        
        if nb_user < nombre:
            print("c'est plus il vous reste", str(essai),  "essai ")

        elif nb_user > nombre:
            print("c'est moins",str(essai) ,"essai ")
        
        elif essai == 10:
            print("perdu")
        else:
            print("bravo vous aver trouver en", str(essai),"essai")
            restart()
jeux()

 





 

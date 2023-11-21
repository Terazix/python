import random

def restart():
    o = input("vouler vous rejouer? ")
    if o == "oui":
        pfc()
    else:
        print("au revoir")
def pfc():
    print("bienvenue dans le jeux du pierre feuille ciseaux")
    choix = ["pierre","feuille","ciseau"]

    while True:
        joueur= input("choissiser pierre feuille ou ciseau pour jouer contre l'ordi ")


        if joueur not in choix:
            print("veuiller saisir la bonne chose")
            continue

        ordinateur = random.choice(choix)

        print(f"l'ordinateur a choisit {ordinateur}")
        if joueur == ordinateur:
                print("egalité")

        elif    (joueur == "pierre" and ordinateur == "ciseau") or (joueur == "feuille" and ordinateur == "pierre") or  (joueur == "ciseau" and ordinateur == "feuille"):
                print("vous aver gagné")

        else:
                print("vous aver perdu")
        restart()
pfc()
import random

def restart():
    yes = input("vouler vous rejouer? ")
    if yes == "oui":
        pfc()
    else:
        print("au revoir")

def pfc():
    print("bienvenue dans le jeux du pierre feuille ciseaux")
    choice = ["pierre","feuille","ciseau"]

    while True:
        user = input("choissiser pierre feuille ou ciseau pour jouer contre l'ordi ")

        if user not in choice:
            print("veuiller saisir la bonne chose")
            continue

        computer = random.choice(choice)

        print(f"l'ordi a choisit {computer}")
        if user == computer:
                print("egalité")

        elif    (user == "pierre" and computer == "ciseau") or (user == "feuille" and computer == "pierre") or  (user == "ciseau" and computer == "feuille"):
                print("vous aver gagné")

        else:
                print("vous aver perdu")
        restart()
pfc()
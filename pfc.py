import random
from tools import *

def start():
    choice: list = ["pierre", "feuille", "ciseau"]
    while True:
        user: str = AskInput("choissiser pierre feuille ou ciseau pour jouer contre l'ordi ", ["pierre","feuille","ciseau"])
        result: dict = {"pierre":0, "feuille":1, "ciseau":2} 
        user_in: str = result[user]
        computer: str = random.choice(choice)
        computer_in: str = result[computer]
        
        res: list = [["egalité","perdu","gagné"],["gagné","egalité","perdu"],["perdu","gagné","egalité"]]
        
        print(f"l'ordi a choisit {computer}",res[user_in][computer_in])
        break

        #if user == computer:
            #print("egalité") 
        
        #elif(user == "pierre" and computer == "ciseau") or (user == "feuille" and computer == "pierre") or  (user == "ciseau" and computer == "feuille"):
            #print("vous aver gagné") 
        
        #else:
            #print("vous aver perdu") 
        
def pfc():
    while True:
        print("bienvenue dans le jeux du pierre feuille ciseaux")
        start()
        yes: str = AskInput("vouler vous rejouer? ",["oui","non"])
        if yes == "oui":
            print("go")
        else:
            print("au revoir")
            break
    
pfc()
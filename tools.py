def AskInput(message: str, choice: list[str]) -> str:
    while True:
        user_in: str = input(message)

        if user_in in choice:
            return user_in

        print("champs non valide")
        print("veuiller reessayer")

def AskInt(message: str) -> int: 
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("entre un truc valide")
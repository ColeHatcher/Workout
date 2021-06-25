from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class printScreen:
    def __init__(self):
        pass

    def printMainMenu(self):
        clear()
        print(mainMenu)

    def printWorkout(self,sets,time):
        clear()
        workout = f"{sets} sets left!\n"
        workout += f"{time} seconds."
        print(workout)
        pass

mainMenu = "Ready to workout\n"
mainMenu += "Press B3"
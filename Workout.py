import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import statHandler
from printScreen import printScreen

logStats = statHandler.statHandler()
display = printScreen()

B1 = KeyCode(char='b')
B2 = KeyCode(char='n')
B3 = KeyCode(char='m')

class Workout:
    def __init__(self):
        self.difficulty = 0

    def startPushups(self):
        startTime = time.time()
        nextTime = startTime + 1
        averagePushup = 0
        if self.difficulty == 0:
            tSets = 3
            for x in range(tSets):
                remainingSeconds = 5
                while remainingSeconds >= 0:
                    if time.time() >= nextTime:
                        display.printWorkout(tSets, remainingSeconds)
                        nextTime = time.time() + 1
                        remainingSeconds -= 1
                    pass
                tSets -= 1

def on_press(key):
    if (key == B1):
        print("Pressed B1")
    elif (key == B2):
        pass
    elif (key == B3):
        pass
    else:
        pass


if __name__ == '__main__':
    display.printMainMenu()
    workout = Workout()
    workout.startPushups()

    #with Listener(on_press=on_press) as listener:
    #    listener.join()
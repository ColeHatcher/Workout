from datetime import date
import json


class statHandler:
    def __init__(self):
        self.stats = [
        ["Total Pushups",0, 0],
        ["Total Situps", 0, 0],
        ["Total Chinups", 0, 0],
        ["Total Pullups", 0, 0],
        ["Total Squats", 0, 0],
        ["Total Burpees", 0, 0],
        ["Plank Length", 0, 0]
    ]

    def changeStat(self,statID,total,time):
        self.stats[statID][1] = 50
        self.stats[statID][2] = 30

    def saveStats(self):
        now = date.today()
        d = f"Workout-{now.month}-{now.day}."
        with open(f'WorkoutStats/{d}', 'w') as save:
            json.dump(self.stats, save)

    def returnStats(self):
        return self.stats
outfile
if __name__ == "__main__":
    logStats = statHandler()
    logStats.changeStat(1,2,2)
    logStats.saveStats()
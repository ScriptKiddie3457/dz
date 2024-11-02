import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print('time to study')
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('time to sleep')
        self.gladness += 3

    def job(self):
        print('time to work')
        self.gladness -= 2
        self.money += random.randint(10, 20)
        self.progress -= 0.05

    def to_chill(self):
        print('time to relax')
        self.gladness += 5
        self.progress -= 0.05
        randmoney = random.randint(5, 20)
        if self.money >= randmoney:
            self.money -= randmoney
        else:
            self.gladness -= 2
            self.job()
        if self.progress > 0.05:
            self.to_study()

    def is_alive(self):
        if self.progress < -0.05:
            print('Too lazy...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False
        elif self.progress > 8:
            print('Genius! Passed!')
            self.alive = False

    def end_of_day(self):
        print(
            f'happiness - {self.gladness} \nprogress - {round(self.progress, 2)} \nmoney - {self.money}$'
        )

    def live(self, day):
        print(f"Day #{day} of {self.name}'s life")
        magic = random.randint(1, 4)
        if magic == 1:
            self.to_study()
        elif magic == 2:
            self.to_sleep()
        elif magic == 3:
            self.to_chill()
        elif magic == 4:
            self.job()
        self.end_of_day()
        self.is_alive()


ryan = Student("Ryan")
for day in range(365):
    if ryan.alive == False:
        break
    ryan.live(day)

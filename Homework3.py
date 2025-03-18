import random as r

class Student:
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.money = r.randint(0, 100)  # Додаємо атрибут грошей
        self.alive = True

    def study(self):
        print('Час для навчання')
        self.happy -= r.randint(1, 50)
        self.progress += r.randint(1, 5)

    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(1, 10)

    def chill(self):
        print('Час для відпочинку')
        self.happy += r.randint(50, 100)
        self.progress -= r.randint(5, 10)
        self.money -= r.randint(5, 20)  # Витрати під час відпочинку

    def work(self):
        print('Час для роботи')
        self.money += r.randint(20, 50)  # Заробіток грошей
        self.happy -= r.randint(5, 15)

    def isAlive(self):
        if self.money <= 0:
            print('У тебе закінчилися гроші! Треба працювати.')
            self.work()
        if self.progress < 2:
            print('Відрахування з інституту')
            self.alive = False
        elif self.progress > 9:
            print('Відмінно навчаєшся')
            self.alive = False
        if self.happy <= 0:
            print('Ти впав у депресію і кинув навчання')
            self.alive = False

    def everyday(self):
        print(f'Рівень щастя: {self.happy}, Прогрес навчання: {self.progress}, Гроші: {self.money}')

    def studyLife(self, day):
        print(f'День №{day}')
        res = r.randint(1, 4)
        if self.money <= 5:
            self.work()
        elif res == 1:
            self.study()
        elif res == 2:
            self.chill()
        elif res == 3:
            self.sleep()
        self.everyday()
        self.isAlive()

st1 = Student('Олег')

print("Життя студента", st1.name)

for k in range(1, 365):  # Студент живе рік
    if not st1.alive:
        break
    st1.studyLife(k)

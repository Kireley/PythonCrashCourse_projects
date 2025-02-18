class Human:
    def __init__(self, gender, age=0, status=1):
        if gender not in ["мужчина", "женщина", "другое"]:
            raise ValueError["Нет такого гендера."]
        self.gender = gender
        self.__age = age
        self.status = status
    def growup(self):
        if self.__age + 1 > 100:
            print("Ой, чел только что сильно повзрослел и умер")
            self.status = 0
        else:
            print(f"С днем рождения, чел! Тебе теперь целых {self.__age + 1} лет!!")
        self.__age += 1

    def get_age(self):
        return self.__age

    def say(self):
        return f"My gender is {self.gender}, I'm {self.status} and {self.__age} years old "

    def __str__(self):
        return f"Я {self.gender}, Я {self.status} и мне {self.__age} лет."

woman = Human("женщина", 5)
print(woman)
woman.growup()
print(woman)


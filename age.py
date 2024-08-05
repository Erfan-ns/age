import datetime


class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name} is {self.height} and age is {self.age}")

    @classmethod
    def birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod
    def adult(age):
        print("yes") if age > 18 else print("no")


p1 = Person.birth("amir", 180, 2001)
p1.show()
Person.adult(23)

import random


class Student:
    position = 0
    name = ''
    age = 0
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
        self.position = self.count

    def info(self) -> None:
        print(f'{self.position} | {self.name} | {self.age}')

    def date(self) -> str:
        return f'{self.position} | {self.name} | {self.age}'

    def __del__(self):
        print(f'deleted obj {self.date()}')


Kota = Student('Kost', 25)
Mare = Student('Maxim', 18)

# print(Kota.name)
# print(Mare.name)

Kota.info()
print(Mare.date())
print(Student.count)

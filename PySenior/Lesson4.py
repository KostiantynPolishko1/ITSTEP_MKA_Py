class Person:
    age: int
    weight: float

    def __init__(self, age: int, weight: float):
        self.age = age
        self.weight = weight

    def info_person(self) -> None:
        print(f'{self.age} - {self.weight}')


class Student(Person):
    name: str
    family: str

    def __init__(self, name: str, family: str, age: int, weight: int):
        Person.__init__(self, age, weight)
        self.name = name
        self.family = family

    def __str__(self):
        return f'{self.name} - {self.family} - {self.age} - {self.weight}'

    def info_worker(self) -> None:
        self.info_person()
        print(f'{self.name} - {self.family}')

    def info_obj(self, name:str, age: int) -> None:
        print(f'{name} : {age}')

# kopo = Student('Kostianyn', 'Polishko', 15, 55)
# kopo.info_worker()
# kopo.age = 10
# kopo.info_worker()
# kopo.info_person()

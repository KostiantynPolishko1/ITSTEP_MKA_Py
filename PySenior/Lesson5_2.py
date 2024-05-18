import tkinter
import inspect

from Lesson4 import Student, Person

# print(help(tkinter))
# print(tkinter.__all__)
# print(dir(tkinter))

# for item in dir(tkinter):
#     print(item)

# for item in dir():
#     print(item)

kopo = Student(name='kopo', family='polo', age=15, weight=55)
# print(kopo)

# print(inspect.getmodule(list))
# print(inspect.getmodule(Student))

myattrs = inspect.signature(Person)

for item in myattrs.parameters.values():
    print(f'{item.name} : {item.default}')
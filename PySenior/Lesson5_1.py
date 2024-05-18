from Lesson4 import Student, Person

kopo = Student(name='kopo', family='polo', age=15, weight=55)
print(kopo)

# print(type(kopo))

# kopoAttributes = list(dir(kopo))
#
# for i in range(len(kopoAttributes)):
#     print(f'{kopoAttributes[i]}')
#
# print(hasattr(kopo, 'name'))
# print(hasattr(kopo, '__str__'))
# print(getattr(kopo, 'family'))
# kopo.age = 22
# print(kopo)
# setattr(kopo, 'name', 'kost')
# print(kopo)
# print(hasattr(kopo, 'info_obj'))
# myInfo = getattr(kopo, 'info_obj')
# myInfo('koxa', 25)
#
# print(type(getattr(kopo, 'info_person')))
# print(type(getattr(kopo, 'info_worker')))
# print(type(getattr(kopo, '__str__')))
#
# print(type(getattr(kopo, 'age')))

# print(issubclass(Student, Person))
# print(isinstance(kopo, Student))
# print(isinstance(kopo, Person))
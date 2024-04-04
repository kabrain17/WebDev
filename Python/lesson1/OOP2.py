class Group:
    name = None

    def __init__(self, name):
        self.name = name


class Student:
    name = None
    group = None

    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __str__(self):
        return f'student: {self.name} | group: {self.group.name}'


csse1603 = Group('CSSE-1603')
csse1605 = Group('CSSE-1605')

aibar = Student('Aibar', csse1603)
madina = Student('Madina', csse1603)
alisher = Student('Alisher', csse1605)
aizhan = Student('Aizhan', csse1605)
daniyar = Student('Daniyar', csse1605)

print(aibar)
print(alisher)
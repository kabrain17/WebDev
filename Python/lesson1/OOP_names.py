class Student:
    name = 'Ivan'
    age = 18
    group_number = '10A'

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, name, age):
        self.name = name
        self.age = age

    def set_group_number(self, group_number):
        self.group_number = group_number

    def show_info(self):
        print(f'{self.name} {self.age} | {self.group_number}')

    @staticmethod
    def print_something():
        print('123123123123123123')


alnur = Student()
alnur.set_name_age('Alnur', 15)
alnur.set_group_number('11B')
madina = Student()
madina.set_name_age('Madina', 14)
madina.set_group_number('10A')
oleg = Student()
oleg.set_name_age('Oleg', 21)
oleg.set_group_number('11A')
ivan = Student()

arr = [alnur, madina, oleg, ivan]

for i in arr:
    i.show_info()
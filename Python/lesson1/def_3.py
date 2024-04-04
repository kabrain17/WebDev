class Soda:
    def __init__(self, dobavka):
        self.dobavka = dobavka

    def show_my_drink(self):
        if type(self.dobavka) == str:
            print(f'Газировка с {self.dobavka}')
        else:
            print(f"Обычная газировка!")


drink3 = Soda('Malina')
print(drink3.show_my_drink())

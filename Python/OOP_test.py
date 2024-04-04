class House:
    _is_house = True
    _street = None
    _number = None
    _floors = 5

    def __init__(self, street, number, is_window = None):
        self._street = street
        self._number = number
        self._is_window = is_window

        if is_window:
            self._is_window = is_window
    def __add__(self, other):
        house3 = House(self._street + other._street, self._number + other._number)
        return house3
    
    def __str__(self):
        return f'House Number: {self._number} | street: {self._street} | {self._is_window}'

    @staticmethod
    def new_method():
        print("Hello")


house1 = House("Abay", 32)
house2 = House("Al-Farabi", 23)
print(house1)
print(house2)
print(house1 + house2)
house1.new_method()
House().new_method

#инкапсуляция это про защиту и договоренность между разработчиками о доступе _ и __ 




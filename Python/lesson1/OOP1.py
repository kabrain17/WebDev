class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):
        if self.side1 <= (self.side2 + self.side3) and self.side2 <= (self.side1 + self.side3) and self.side3 <= (self.side2 + self.side1):
            print("True")
        else:
            print("False")

res = Triangle(1, 2, 3)
print(res.is_triangle())




class MyShape:
    def __init__(self, color="black", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0

shape = MyShape("blue", False)
print(shape)
print("Area:", shape.getArea())
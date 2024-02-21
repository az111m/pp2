def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
a = int(input("'A' number: "))
b = int(input("'B' number: "))
my_numbers = squares(a, b)
for j in my_numbers:
    print(j)
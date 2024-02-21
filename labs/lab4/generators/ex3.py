def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input('The number: '))
my_numbers = divisible(n)
for j in my_numbers:
    print(j)

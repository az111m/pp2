def square_numbers(n):
    for i in range(1, n + 1):
            yield(i*i)
n = int(input('Some number: '))
my_numbers = square_numbers(n)
for j in my_numbers:
      print(j)
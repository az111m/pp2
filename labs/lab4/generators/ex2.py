def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Number: "))
even_gen = even_numbers(n)
my_numbers = [str(num) for num in even_gen]
print(', '.join(my_numbers))
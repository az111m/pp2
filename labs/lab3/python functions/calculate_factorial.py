def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
num = int(input('The number: '))
if num < 0:
    print('Impossible')
else:
    print('Factorial is', calculate_factorial(num))
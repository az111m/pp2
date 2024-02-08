def reverse_string(str):
    l = list(str)
    l.reverse()
    str_2 = "".join(l)
    return str_2
str_1 = str(input('String: '))
print(reverse_string(str_1))
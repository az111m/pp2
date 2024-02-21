import math

num = int(input('Number of sides: '))
len = int(input('Length of a side: '))
pi = math.pi
cos = math.cos(pi/num)
sin = math.sin(pi/num)
len_square = pow(len, 2)
area = num / 4 * len_square * (cos / sin)
print('Area: ' + str(area))
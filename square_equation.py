# Даны три вещественных числа a, b, c. Программа находит вещественные корни квадратного уравнения.

from math import *

a = float(input())
b = float(input())
c = float(input())
d = pow(b, 2) - (4 * a * c)

if d == 0:
    x = -b / (2 * a)
    print(x)
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
else:
    print('Вещественных корней нет')
# Программа определяет, является ли год с данным номером високосным.
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')
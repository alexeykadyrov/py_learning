# На вход программе подаются 4 целых числа a1, b1, a2, b2. Гарантируется что a1 < b1 и a2 < b2.
# Программа выводит на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 < a2 or b2 < a1:
   print('пустое множество')
elif a2 == b1:
   print(a2)
elif b2 == a1:
   print(b2)
elif a2 >= a1 and b2 <= b1:
   print(a2, b2)
elif a1 >= a2 and b1 <= b2:
   print(a1, b1)
elif a1 < a2 < b1 and a2 < b1 < b2:
   print(a2, b1)
elif a2 < a1 < b2 and a1 < b2 < b1:
   print(a1, b2)
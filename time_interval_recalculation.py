# Программа для пересчёта величины временного интервала.
# Время заданное в минутах, пересчитывается в величину, выраженную в часах и минутах.

t = int(input())
print(t, 'мин - это', t // 60, 'час', t % 60, 'минут', end='.')
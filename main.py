from math import *
x = float(input('Введите х '))
if x > 7.7:
    y = log(x) * sin(3*x)
elif x == 7.7:
    y = (x**5 - 1)**1/5
else:
    y = 1 + cos(2*x)**3 - 3*sin(3*x)**2
print('y =',y)
#задание 2
n = int(input('Введите год '))
if n % 4 == 0 and n % 100 != 0:
    print('Этот год високосный')
elif n % 4 == 0 and n % 400 == 0:
    print('Этот год високосный')
else:
    print('Этот год не високосный')
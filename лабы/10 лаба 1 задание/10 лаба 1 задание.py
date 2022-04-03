import math
from random import randint

pi = 3.14

def function():
    for i in range(0, 5):
        r = randint(10, 10000)
        s = pi * r**2
        print(round(s, 4))
function()

# Напишите генератор, который бы возвращал площади кругов 
# с радиусами в диапазоне от 10 до 10 000. Вывести на экран первые пять значений 
# с точностью до сотых. 
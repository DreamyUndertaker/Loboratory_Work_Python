import abc
from copyreg import pickle
import random, pickle
a = []

for i in range(100):
    a.append(random.randint(0, 10))
print(a)

with open("file.bin", "wb") as file:
    pickle.dump(a, file)

with open("file.bin", "rb") as file:
    abc = pickle.load(file)
    x = file
    a.append(x)
print(a)

# Импортируйте в программу стандартный модуль random и, 
# используя одноименную функцию random, сгенерируйте 100 случайных чисел. 
# Все эти числа следует представить в виде списка, сформированного с помощью генератора списков. 
# Сохраните полученные данные в файл в бинарном режиме доступа. Затем, 
# прочитайте из него данные и поместите в другой список. Выведите на экран полученный список 
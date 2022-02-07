real_Number = input().split(" ")
real_Number = [float(i) for i in ssd]
real_Number = [j for j in ssd if j % 2 == 0]
if real_Number:
    small_Number = real_Number[0]
    for i in real_Number:
        if i < small_Number:
            small_Number = i
            print(small_Number)
        else:
            print(None)
# вводится список в виде вещественных чисел в одну строку через пробел.
# С помощью цикла for необходимо найти наименьшее четное значение в этом списке.
# Полученый результат вывести на экран. Если четного значения нет, то вывести "None".
# Без функции min.

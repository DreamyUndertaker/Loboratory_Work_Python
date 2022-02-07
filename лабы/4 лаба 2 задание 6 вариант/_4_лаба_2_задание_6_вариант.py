real_Number = input()
d = []

for i in range(len(real_Number)):
    if real_Number[i] == real_Number[i - 1]:
        d.append(real_Number[i])
        if d == []:
            print("Нет")
        else: 
            print(d)
# Вводится натуральное число. Необходимо проверить, есть ли в этом числе какие-либо одинаковые цифры,
# стоящие рядом. Вывести эти цифры, если такие есть, иначе вывести "Нет"
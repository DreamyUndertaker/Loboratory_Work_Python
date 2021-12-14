real_Number = input()
d = []

for i in range(len(real_Number)):
    if real_Number[i] == real_Number[i - 1]:
        d.append(real_Number[i])
        if d == []:
            print("Нет")
        else: 
            print(d)
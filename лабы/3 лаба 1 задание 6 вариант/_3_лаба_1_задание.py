a = int(input())
b = int(input())
d = int(input())

if a == b:
    if d + 1 < a:
        print("Да")
    else:
        print("Нет")
else:
    if a < b:
        if d + 1 < a:
            print("да")
        else:
            print("нет")
    else:
        print("нет")

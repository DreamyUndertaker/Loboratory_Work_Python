s=input()
a=[int(s) for s in s.split()]

for i in a:
    if int(i) > 0:
       i = i + i
print(i, end=' ')
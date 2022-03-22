from re import A

dictionary = {}
def zad1 (a):
    return(a, len(a))

word = input().split()

i = 0
a = ()

while (len(word) != i):
    a = a + zad1(word[i])
    i = i + 1

i = 0
f = 0
while (len(word)):
    d = {}
    i = i + 1

print(a)
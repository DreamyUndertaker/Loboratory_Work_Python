n = int(input())
lst = [[i for _ in range(n)] for i in range(n)]
print(*lst, sep = '\n')
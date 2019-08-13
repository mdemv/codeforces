# https://codeforces.com/problemset/problem/50/A

# https://codeforces.com/blog/entry/1006
# Кошерное решение:  floor(N*M*0.5). Поскольку на доске N*M клеток, и каждая доминошка покрывает ровно 2 клетки, то больше положить точно нельзя

import math

m, n = input().split(" ")
m, n = int(m), int(n)

#print(m * n)
total = m * n
i = 0
result = 0
for i in range(9999):
    if (2 * i) > total:
        result = i - 1
        break

print(result)

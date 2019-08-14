# https://codeforces.com/problemset/problem/263/A

import math

y_shift = 0
x_shift = 0

for i in range(5):
    row = input().replace(" ", "")
    if(row.find("1")) != -1:
        y_shift = int(math.fabs(3 - (i + 1)))
        x_shift = int(math.fabs(3 - (row.find("1") + 1)))

print(y_shift + x_shift)

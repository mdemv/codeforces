# https://codeforces.com/problemset/problem/96/A

import sys

situation = input()

for k in range(len(situation)):
    if situation[k:k+7] == "0000000" or situation[k:k+7] == "1111111":
        print("YES")
        sys.exit()

print("NO")

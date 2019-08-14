# https://codeforces.com/problemset/problem/112/A

import sys

str1 = input().lower()
str2 = input().lower()

str_len = len(str1)

for i in range(str_len):
    if ord(str1[i]) < ord(str2[i]):
        print("-1")
        sys.exit()
    elif ord(str1[i]) > ord(str2[i]):
        print("1")
        sys.exit()

print("0")
sys.exit()

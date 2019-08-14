# https://codeforces.com/problemset/problem/339/A

str = input()

arr1 = str.split('+')
arr1.sort()
print("+".join(arr1))

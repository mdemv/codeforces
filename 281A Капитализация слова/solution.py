# https://codeforces.com/problemset/problem/281/A

word = input()

arr = list(word)
arr[0] = arr[0].upper()
word1 = "".join(arr)

print(word1)

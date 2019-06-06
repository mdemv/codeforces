# http://codeforces.com/problemset/problem/4/A

w = input()

if int(w) == 2:
  print("NO")
  exit()

if int(w) / 2 == int(w) // 2:
  print("YES")
else:
  print("NO")
exit()

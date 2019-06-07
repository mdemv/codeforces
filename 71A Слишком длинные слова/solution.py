# https://codeforces.com/problemset/problem/71/A

linestotal = input()

r = []
for line in range(int(linestotal)):
    w = input()
    if len(w) > 10:
      r.append(w[0] + str(len(w) - 2) + w[-1])
    else:
      r.append(w)

for word in r:
  print(word)

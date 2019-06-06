# http://codeforces.com/problemset/problem/1/A

def test(n, m, a):
  return

args = input()
argsArr = args.split(" ", 3)

n = int(argsArr[0])
m = int(argsArr[1])
a = int(argsArr[2])
plitN = 0
plitM = 0

if(n // a != n / a):
  plitN = n // a + 1
else:
  plitN = n // a
if(m // a != m / a):
  plitM = m // a + 1
else:
  plitM = m // a

print(plitN * plitM)

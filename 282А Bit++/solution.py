# https://codeforces.com/problemset/problem/282/A

total_ops = input()

x = 0;
for k in range(int(total_ops)):
    op = input()
    if(op.find("+")) != -1:
        x += 1
    else:
        x -= 1

print(x)

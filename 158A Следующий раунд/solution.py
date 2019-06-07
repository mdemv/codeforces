# https://codeforces.com/problemset/problem/158/A

n_k_string = input()
n_k_arr = n_k_string.split(" ")
total_uchastnikov = n_k_arr[0]
mesto_k = n_k_arr[1]

scores_string = input()
scores_arr = scores_string.split(" ")

score_on_k = scores_arr[int(mesto_k) - 1]

i = 0
for s in scores_arr:
  if int(s) >= int(score_on_k) and int(s) > 0:
    i += 1

print(i)

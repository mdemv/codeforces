# https://codeforces.com/problemset/problem/231/A

# Жадный алгоритм — алгоритм, заключающийся в принятии локально оптимальных решений на каждом этапе,
# допуская, что конечное решение также окажется оптимальным.

total_issues = input()
#print(total_issues)

issues_to_solve = 0
for issue in range(int(total_issues)):
  solutions = input()
  solutionsArr = solutions.split(" ")
  a, b, c = int(solutionsArr[0]), int(solutionsArr[1]), int(solutionsArr[2])
  if((a + b + c) >= 2):
      issues_to_solve += 1

print(issues_to_solve)

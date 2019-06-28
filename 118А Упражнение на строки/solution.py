# https://codeforces.com/problemset/problem/118/A

str = input()
glasn = ["A", "O", "Y", "E", "U", "I"]

result = []
for letter in str:
  if(letter.upper() not in glasn):
    result.append("." + letter.lower())

print("".join(result))

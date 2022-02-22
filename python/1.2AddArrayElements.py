
def sum (n, s):
  result = 0
  for i in range(0, n):
    print(i, '\n')
    result = result + s[i]
  return result

S = [-1, 10, 7, 11, 5, 13, 8]
sum = sum(len(S), S)
print('sum =', sum)
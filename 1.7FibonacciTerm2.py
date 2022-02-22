"""재귀적으로 똑같은 값이 계산되는 일이 없게 값을 미리 구해놓고
   구한 값으로 다음 값을 구하는데 이용함
   실행 시간이 매우 빠름을 알 수 있다 즉, 효율성이 매우 높다
"""
# Iterative
def fib2(n):
  f = [0] * (n + 1)
  if (n > 0):
    f[1] = 1
    for i in range(2, n + 1):
      f[i] = f[i - 1] + f[i - 2]
  return f[n]


# for i  in range(50):
#   print(fib2(i), end=" ")


  """
  리스트 f를 사용하지 않고도 피보나치 항을 구할 수 있을까?
  """
def fib3(n):
  arg1 = 0
  arg2 = 1
  if (n <= 1):
    return n
  else:
    for i in range(2, n + 1):
      temp = arg2
      arg2 = arg1 + arg2
      arg1 = temp
  return arg2

print(fib3(7))
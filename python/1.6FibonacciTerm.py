# Recursive
def fibonacci(n):
  if (n <= 1):
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(50):
  print(fibonacci(i), end=" ")


  # 피보나치 알고리즘의 효율성
  # 재귀적 정의 이용 : 작성하기도 쉽고, 이해하기도 쉽다
  # 그러나 너무 비효율적임 왜?

"""
  fib(5)는 내부적으로 (fib(4), fib(3)을 호출하고 이렇게 호출하면서
  내부적으로 동일한 함수를 호출하는 경우가 생긴다 이는 중복된 함수를 호출
  하는 면에 있어서 비 효율적이라고 볼 수 있다. 
"""
  
# 큰 정수의 덧셈
def lAdd(u, v):
  n = len(u) if (len(u) > len(v)) else len(v) # 3항 연산자로 두개의 리스트중 더 긴 리스트를 선택
  result = []
  carry = 0
  for k in range(n):
    i = u[k] if (k < len(u)) else 0 # 자리수가 없으면 0으로 대치
    j = v[k] if (k < len(v)) else 0
    value = i + j + carry
    carry = value // 10
    result.append(value % 10)
  if carry > 0:
    result.append(carry)
  return result

# 큰 정수의 뺄셈
def lSub(u, v):
  n = len(u) if (len(u) > len(v)) else len(v) # 3항 연산자로 두개의 리스트중 더 긴 리스트를 선택
  result = []
  borrow = 0
  for k in range(n):
    i = u[k] if (k < len(u)) else 0 # 자리수가 없으면 0으로 대치
    j = v[k] if (k < len(v)) else 0
    value = i - j + borrow
    if value < 0:
      value += 10
      borrow = -1
    else:
      borrow = 0
    result.append(value % 10)
  if (borrow < 0):
    print("음의 정수는 처리하지 못함.")
  return result

u = [3, 2, 1]
v = [5, 4]
print(123 + 45)
print(lAdd(u, v)[::-1])


u2 = [6, 7, 8, 9]
v2 = [3, 4, 5]
print(9876 + 543)
print(lAdd(u2, v2)[::-1])

u3 = [2, 3, 8, 7, 6, 5]
v3 = [3, 2, 7, 3, 2, 4, 9]
print(567832 + 9423723)
print(lAdd(u3, v3)[::-1])


# 큰 정수의 곱셈 : 자릿수 나누기
def prod(u, v):
  n = len(u) if (len(u) > len(v)) else len(v)
  if (len(u) == 0 or len(v) == 0):
    # print(u, v, [0])
    return [0]
  elif (n <= threshold):   # 일정값으로 자릿수 줄어들면 곱하기 진행
    return lMult(u, v)     # 실제 곱하기
  else:
    m = n // 2
    x = div(u, m)
    y = rem(u, m)
    w = div(v, m)
    z = rem(v, m)
    p1 = prod(x, w)
    p2 = lAdd(prod(x, z), prod(w, y))
    p3 = prod(y, z)
    return lAdd(lAdd(exp(p1, 2*m), exp(p2, m)), p3)

# 큰 정수의 효율적인 곱셈
def prod2(u, v):
  n = len(u) if (len(u) > len(v)) else len(v)
  if (len(u) == 0 or len(v) == 0):
    # print(u, v, [0])
    return [0]
  elif (n <= threshold):   # 일정값으로 자릿수 줄어들면 곱하기 진행
    return lMult(u, v)     # 실제 곱하기
  else:
    m = n // 2
    x = div(u, m)
    y = rem(u, m)
    w = div(v, m)
    z = rem(v, m)
    r = prod2(lAdd(x, y), lAdd(w, z))
    p1 = prod2(x, w)
    p3 = prod2(y, z)
    p2 = lSub(r, lAdd(p1, p3))
    return lAdd(lAdd(exp(p1, 2*m), exp(p2, m)), p3)

# 10의 제곱
def exp(u, m):
  if (u == [0]):
    return [0]
  else:
    return ([0] * m) + u

# 나누기
def div(u, m):
  if (len(u) < m):
    u.append(0)
  return u[m : len(u)]

# 나머지
def rem(u, m):
  if (len(u) < m):
    u.append(0)
  return u[0 : m]

# threshold가 1인 경우의 곱셈만 계산됨
def lMult(u, v):
  i = u[0] if (0 < len(u)) else 0
  j = v[0] if (0 < len(v)) else 0
  value = i * j
  carry = value // 10
  result = []
  result.append(value % 10)
  if (carry > 0):
    result.append(carry)
  return result


u4 = [2, 3, 8, 7, 6, 5]
v4 = [3, 2, 7, 3, 2, 4, 9]
print(exp(v4, 4)[::-1])
print(div(v4, 4)[::-1])
print(rem(v4, 4)[::-1])


# 최종 큰 수의 곱셈 해보기
threshold = 1 # 임계치는 1임
u = [2, 3, 8, 7, 6, 5] # 567,832
v = [3, 2, 7, 3, 2, 4, 9] # 9,423,723\
print(567832 * 9423723)
print(prod2(u, v)[::-1])
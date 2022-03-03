from turtle import st


def strassen(A, B):
  n = len(A)
  if n <= threshold:
    return matrixMult(A, B)
  A11, A12, A21, A22 = divide(A)
  B11, B12, B21, B22 = divide(B)
  M1 = strassen(mAdd(A11, A22), mAdd(B11, B22))
  M2 = strassen(mAdd(A21, A22), B11)
  M3 = strassen(A11, mSub(B12, B22))
  M4 = strassen(A22, mSub(B21, B11))
  M5 = strassen(mAdd(A11, A12), B22)
  M6 = strassen(mSub(A21, A11), mAdd(B11, B12))
  M7 = strassen(mSub(A12, A22), mAdd(B21, B22))
  return conquer(M1, M2, M3, M4, M5, M6, M7)

# n>2 인 nxn 행렬을 쉬트라센 곱을 이용하기 위해 쪼갠다.
def divide(A):
  n = len(A)
  m = n // 2
  A11 = [[0] * m for _ in range(m)]
  A12 = [[0] * m for _ in range(m)]
  A21 = [[0] * m for _ in range(m)]
  A22 = [[0] * m for _ in range(m)]
  for i in range(m):
    for j in range(m):
      A11[i][j] = A[i][j]
      A12[i][j] = A[i][j + m]
      A21[i][j] = A[i + m][j]
      A22[i][j] = A[i + m][j + m]
  return A11, A12, A21, A22

# 분할한 행렬들을 각각 정복하기
def conquer(M1, M2, M3, M4, M5, M6, M7):
  C11 = mAdd(mSub(mAdd(M1, M4), M5), M7)
  C12 = mAdd(M3, M5)
  C21 = mAdd(M2, M4)
  C22 = mAdd(mSub(mAdd(M1, M3), M2), M6)

  m = len(C11)
  n = 2 * m
  C = [[0] * n for _ in range(n)]
  for i in range(m):
    for j in range(m):
      C[i][j] = C11[i][j]
      C[i][j + m] = C12[i][j]
      C[i + m][j] = C21[i][j]
      C[i + m][j + m] = C22[i][j]
  return C

# 행렬 덧셈
def mAdd(A, B):
  n = len(A)
  C = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] + B[i][j]
  return C

# 행렬 뺄셈
def mSub(A, B):
  n = len(A)
  C = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] - B[i][j]
  return C

# 행렬곱셈
def matrixMult(A,B):
  n = len(A)
  C =[[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C

threshold = 2
A = [
  [1, 2, 3, 4, 1, 2, 3, 4],
  [5, 6, 7, 8, 5, 6, 7, 8],
  [9, 1, 2, 3, 9, 1, 2, 3],
  [4, 5, 6, 7, 4, 5, 6, 7],
  [1, 2, 3, 4, 1, 2, 3, 4],
  [5, 6, 7, 8, 5, 6, 7, 8],
  [9, 1, 2, 3, 9, 1, 2, 3],
  [4, 5, 6, 7, 4, 5, 6, 7]
]

B = [
  [8, 9, 1, 2, 8, 9, 1, 2],
  [3, 4, 5, 6, 3, 4, 5, 6],
  [7, 8, 9, 1, 7, 8, 9, 1],
  [2, 3, 4, 5, 2, 3, 4, 5],
  [8, 9, 1, 2, 8, 9, 1, 2],
  [3, 4, 5, 6, 3, 4, 5, 6],
  [7, 8, 9, 1, 7, 8, 9, 1],
  [2, 3, 4, 5, 2, 3, 4, 5]
]

print("threshold = ", threshold)
print("A = ", A)
print("B = ", B)
C = strassen(A, B)
for i in range(len(C)):
  print("C[%d] = "%(i), C[i])
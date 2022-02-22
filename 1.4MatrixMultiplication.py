# 행렬의 곱 : (A X B), (B X C)의 행렬을 곱하면 A X C의 행렬이 반환된다.

def matrixMult(A, B):
  r = len(A)
  c = len(B[0])
  print(r)
  d = [[0] * c for _ in range(r)]  # _ : 딱히 사용하지 않으므로 dummy처리
  for i in range(r):
    for j in range(c):
      for k in range(len(A[0])):
        d[i][j] += A[i][k] * B[k][j]
  return d


A = [[2, 3, 2, 2], [4, 1, 4, 4], [4,2,3, 6]]
B = [[5, 7], [6, 8], [1, 2], [2,5]]

d = matrixMult(A, B)
for i in range(len(d)):
  for j in range(len(d[i])):
    print(d[i][j], end=" ")
  print()
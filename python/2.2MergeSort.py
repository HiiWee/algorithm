# Algorithm 2.2 : MergeSort (2.3 Merge)
def mergeSort(S):
  n = len(S)
  if (n <= 1):
    return S
  else:
    mid = n // 2
    U = mergeSort(S[0 : mid])
    V = mergeSort(S[mid : n])
    return merge(U, V)

def merge(U, V):
  print("U = " , U, " V = " , V)
  S = []
  i = j = 0
  while (i < len(U) and j < len(V)):
    if (U[i] > V[j]):
      S.append(V[j])
      j += 1
    else:
      S.append(U[i])
      i += 1
  if (i < len(U)):
    S += U[i : len(U)]
  else:
    S += V[j : len(V)]
  return S

S = [27, 10, 13, 20, 25, 13, 15, 22]
newS = mergeSort(S)
print(newS)

'''
* Algorithm 2.2/2.3의 문제점
  * 입력 리스트 S이외에 리스트 U와 V를 추가적으로 사용
  * 메모리 사용의 비 효율성: 더 효율적인 방법은 없을까?

* 추가적으로 만들어지는 리스트 원소의 총 수
  * mergeSort()를 호출할 때마다 U와 V를 새로 생성함
  * 첫번째 재귀 호출시 원소의 개수가: U가 n/2개, V가 n/2개 (대략 n개)
  * 두번째 재귀 호출시 U가 n/4개, V가 n/4개 (대략 n/2개)
  * 따라서 전체 재귀 호출시 원소의 개수: n + n/2 + n/4 + ... = 2n(대략 2n개 정도)
  * 값을 전달할 때 리스트가 아닌 low, high값만 넘겨줘서 S리스트 하나와 임시 리스트 1개로 해결하면 됨
  * 이렇게 되면 대략 n개 정도로 공간을 절약할 수 있다.
'''
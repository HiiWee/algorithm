# Algorithm 2.4: Merge Sort2 (Enhanced Merge Sort)
def mergeSort2(S, low, high):
  if (low < high):
    mid = (low + high) // 2
    mergeSort2(S, low, mid)
    mergeSort2(S, mid + 1, high)
    print(S[low:high+1])
    merge2(S, low, mid, high)

# Algorithm 2.5: Merge2 (Enhanced Merge)
def merge2(S, low, mid, high):
  i = low
  j = mid + 1
  U = []
  while (i <= mid and j <= high):
    if (S[i] < S[j]):
      U.append(S[i])
      i += 1
    else:
      U.append(S[j])
      j += 1
  if (i <= mid):
    U += S[i : mid + 1]
  else:
    U += S[j : high + 1]
  for k in range(low, high + 1):
    S[k] = U[k - low]

S = [27, 10, 13, 20, 25, 13, 15, 22]
mergeSort2(S, 0, len(S) - 1)
print(S) 

'''
추가적으로 만들어지는 원소의 수를 약 n개 정도로 절약

Divid-and-conquer :분할정복 알고리즘 설계 기법을 배움
  1. 이진 탐색
  2. 합병 정렬
  이진 탐색은 반을 취하고 나머지는 버리는 것을 반복
  합병 정렬은 반을 쪼개며 들어가며 양쪽을 해결하며 하나씩 합병
  따라서 시간복잡도는 이진탐색이 더 우수
'''
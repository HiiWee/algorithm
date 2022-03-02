def quickSort(S, low, high):
    if (high > low):
        pivotPoint = partition(S, low, high)
        quickSort(S, low, pivotPoint - 1)
        quickSort(S, pivotPoint + 1, high)

# Algoritm2.7 Partition : partition알고리즘은 퀵소트 뿐아니라 여러가지 알고리즘에서 많이 사용된다.
# 아래의 partition함수는 보편적으로 쓰이는 방법이 아니다.
def partition(S, low, high):
    pivotItem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        print(i, j, S)  # 정렬과정을 확인하기 위한 print()
        if (S[i] < pivotItem):
            j += 1
            S[i], S[j] = S[j], S[i] #swap
    pivotPoint = j
    S[low], S[pivotPoint] = S[pivotPoint], S[low] #swap
    return pivotPoint

# 보편적인(많이 사용되는) Partition함수 구현
def partition2 (S, low, high):
    pivotItem = S[low]
    i = low + 1
    j = high
    while (i <= j):
        while (i <= high and S[i] < pivotItem):
              i += 1
        while (j >= low and S[j] > pivotItem):
              j -= 1
        if (i < j):
            S[i], S[j] = S[j], S[i]
        print(i, j, S)
    pivotPoint = j
    S[low], S[pivotPoint] = S[pivotPoint], S[low]
    return pivotPoint

def quickSort2 (S, low, high):
    if (high > low):
        pivotPoint = partition2(S, low, high)
        # print(S)
        quickSort2(S, low, pivotPoint - 1)
        quickSort2(S, pivotPoint + 1, high)

S = [15, 22, 13, 27, 12, 10, 20, 25]
print("before : ", S)
quickSort2(S, 0, len(S) - 1)
print("after : ", S)
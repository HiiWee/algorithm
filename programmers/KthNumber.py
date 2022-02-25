def solution(array, commands):
    i = 0
    j = 0
    first = 0
    second = 0
    third = 0
    
    answer = []
    # i, j, k 값을 나누기
    while(i < len(commands) and j < 3):
        for j in range(0, 3):
            if (j == 0):
                first = commands[i][j]
            elif (j == 1):
                second = commands[i][j]
            else:
                third = commands[i][j]
                i += 1
            
        beforeSort = array[first - 1 : second]
        sort(beforeSort, 0, len(beforeSort) - 1)
        answer.append(beforeSort[third - 1])
        
    return answer

# 합병 정렬 사용
def sort(beforeSort, low, high):
    if (low < high):
        mid = (low + high) // 2
        sort(beforeSort, low, mid)
        sort(beforeSort, mid + 1, high)
        merge(beforeSort, low, mid, high)
        
# 합병 과정
def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = 0
    temp = []
    while (i <= mid and j <= high):
        if (arr[i] > arr[j]):
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1
    if (i <= mid):
        temp += arr[i : mid + 1]
    else:
        temp += arr[j : high + 1]
    for k in range(low, high + 1):
        arr[k] = temp[k - low]
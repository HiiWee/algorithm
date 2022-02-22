def binSearch(n, arr, x):
  low = 0
  high = n - 1
  location = 0

  while (low <= high and location == 0):
    mid = (low + high) // 2   # 정수 몫만 남기고 소수점 아래는 버림
    if (x == arr[mid]):
      location = mid
    elif(x < arr[mid]):
      high = mid - 1
    else:
      low = mid + 1
  return location

arr = [12, 15, 16, 26, 34, 56, 77]
location = binSearch(len(arr), arr, 56)
print(location)
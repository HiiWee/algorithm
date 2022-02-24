def binarySearch(S, low, high):
  if (low > high):
    return 0
  else:
    mid = (low + high) // 2
    if (x == S[mid]):
      return mid
    elif(x > S[mid]):
      return binarySearch(S, mid + 1, high)
    else:
      return binarySearch(S, low, mid - 1)


S = [1, 5, 8, 13, 55, 67, 134, 787]
x = 787

print(binarySearch(S, 0, len(S)))
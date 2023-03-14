arr = [3,1,5,2,7,0,6]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)


def binarySearch(arr, left, right, item):
    if (left <= right):
        mid = (left + right) // 2
        if (arr[mid] == item):
            return mid
        elif (arr[mid] > item):
            return binarySearch(arr, left, mid - 1, item)
        else:
            return binarySearch(arr, mid + 1, right, item)
    else: 
        return -1 

print(binarySearch(arr, 0, len(arr) -1, 6))
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80]
key = 70

result = binary_search(arr, key)
if result == -1:
    print("Key is Not Present...!")
else:
    print("Index:", result)

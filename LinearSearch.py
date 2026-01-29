def linearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return 1

array = [10,50,40,20,5,35]
result = linearSearch(array,5)

if result == -1:
    print("Element Not Present In List...!")
else:
    print(f"Element fount at location {result+1}")
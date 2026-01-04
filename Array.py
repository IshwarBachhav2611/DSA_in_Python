#Array Creation 
arr = [10,20,30,40,50]

#Accesing Array Elements 
print("Array :",arr)
print("Array First Element :",arr[0])
print("Array last Element :",arr[-1])
print("Lengt of Array :",len(arr))

#Traversing Array 
for i in range(len(arr)):
    print(arr[i])

#Insert Element 
arr.insert(0,101) #at start 
arr.append(102) #at last 
arr.insert(3,103) #at position
print("Array :",arr)


#Delete Element 
arr.remove(30) #specific element in array
arr.pop(3) # 103
#elemet on index default last elemet 
print("Array :",arr)

#update Elements


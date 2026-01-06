Arr = [10,20,30,40,50,60,70,80,90,100]
print("Array : ",Arr )
key = int(input("Enter Element To find :"))

for i in range(len(Arr)):
    if Arr[i] == key:
        print("location Array[",i,"] =",key)
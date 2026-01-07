#Search in 2D Array
Arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]

print("Matrix :")
for i in Arr:
    print(i,end="\n")

key = int(input("Enter Element To Find :"))

for i in range(len(Arr)):
    for j in range(len(Arr[0])):
        if Arr[i][j] == key:
            print(f"Elemet :{key}, Position Arr[",i,"][",j,"]")
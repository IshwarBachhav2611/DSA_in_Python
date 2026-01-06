#Create Two Dimensional Array
Arr = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]

#Access Element 
print(Arr[0][0])# first element
print(Arr[1][1])# randome element
print(Arr[-1][-1])# first element

#2D Traverse Array
print(" 2D Array Traverse :")
for i in range(len(Arr)):
    for j in range(len(Arr)):
        print(Arr[i][j],end=" ")
    print(end="")

#Insert Row
print("After Inserting Row :")
row = [100,101,103]
Arr.append(row)
for i in Arr:
    print(i,end="\n")

#Insert Columan
print("After Inserting Column: ") 
col = [100, 200, 300, 400]
for i in range(len(Arr)):
    Arr[i].append(col[i])

for i in Arr:
    print(i,end="\n")

#Delete Element 
print("After Removing Row: ")
Arr.pop(3)
for i in Arr:
    print(i,end="\n")

#Delete Column
print("After Removing Columan: ")
for i in range(len(Arr)):
    Arr[i].pop()
for i in Arr:
    print(i,end="\n")

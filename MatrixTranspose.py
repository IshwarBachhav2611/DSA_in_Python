#Matrix Transpose

Arr = [
    [10,20,30],
    [40,50,60],
    ]

row = len(Arr)
col = len(Arr[0])

transpose = [[0]*row for _ in range(col)] # this line create No. Columns = no. element in row 

for i in range(row):
    temp = []
    for j in range(col):
        transpose[j][i]=Arr[i][j]

print("Before Transpose :")
for i in Arr:
    print(i,end="\n")

print("After Transpose :")
for i in transpose:
    print(i,end="\n")
    


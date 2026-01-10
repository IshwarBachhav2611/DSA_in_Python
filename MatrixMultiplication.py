#Matrix Addition
matrix1 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]

matrix2 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]

matrix3 = []


for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1[0])):
        temp.append(matrix1[i][j]*matrix2[i][j])
    matrix3.append(temp)
    del temp

#print Output
print("Matrix 1:")
for i in matrix1:
    print(i,end="\n")

print("Matrix 2:")
for i in matrix2:
    print(i,end="\n")
    
print("Multiplication of Matrix1 and Matrix2 :")
for i in matrix3:
    print(i,end="\n")

# Sparse Matrix 
Matrix = [
        [0,0,1],
        [2,0,0],
        [0,0,3]
    ]
zero = 0
non_zero = 0
# Check if Matrix is Sparse or Not
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        if Matrix[i][j] == 0:
            zero = zero+1
        else:
            non_zero = non_zero+1

for i in Matrix:
    print(i,end="\n")

if zero>non_zero:
    print("Sparse Matrix :")
else:
    print("Normal Matrix :")

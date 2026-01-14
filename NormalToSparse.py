# Normal Matrix To Sparse Matrix Conversion 

normal = [
        [0,0,1],
        [0,2,0],
        [3,0,0]
    ]
sparse = []

for i in range(len(normal)):
    for j in range(len(normal[0])):
            if normal[i][j] != 0:
                value = normal[i][j]
                sparse.append([i,j,value])
            
for i in sparse:
     print(i,end="\n")
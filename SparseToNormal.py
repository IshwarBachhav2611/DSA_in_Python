# Sparse Matrix To Normal MAtrix Conversion 

sparse = [
    [0, 2, 1],
    [1, 1, 2],
    [2, 0, 3]
    ]

row = len(sparse)
col = len(sparse[0])

normal = [[0]*col for _ in range(row) ]

for item in sparse:
    R,C,V = item
    normal[R][C] = V
        

for i in normal:
    print(i,end="\n")
array = [
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,2],
    [0,0,0,0,0,1,2,3],
    [0,0,0,0,1,2,3,4],
    [0,0,0,1,2,3,4,5]
]

for i in range(len(array)) :
    for j in range(len(array[i])) :
        print(array[i][j],end='')
    print()
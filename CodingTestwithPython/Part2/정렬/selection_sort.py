array = [7,5,9,0,3,1,6,2,4,8]

# 선택 정렬

for i in range(len(array)) :
    # 가장 작은 인덱스를 i로 둔다
    min_index = i
    for j in range(i+1,len(array)) :
        # i+1부터 array 끝까지 모두 세어서 가장 작은 값을 구한다
        if array[min_index] > array[j] :
            min_index = j
    # 가장 작은 값을 i번째 값과 서로 맞바꾼다
    array[min_index], array[i] = array[i], array[min_index]

# 선택정렬의 시간 복잡도는 O(N^2)임. ( 정확히는 (N^2 + N) / 2 )
print(array)

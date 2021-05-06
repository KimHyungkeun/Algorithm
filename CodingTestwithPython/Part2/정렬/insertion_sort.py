array = [7,5,9,0,3,1,6,2,4,8]

# 삽입 정렬

for i in range(1, len(array)) :
    # 0번째는 이미 정렬되어있다고 가정하므로, 1번째부터 시작한다
    for j in range(i, 0, -1) :
        # i번째를 기준으로 거꾸로 바라보며, 본인보다 큰 수를 발견하면 그 수의 이전 단계로 자리를 옮긴다.
        if array[j-1] > array[j] :
            # 큰 수와 작은수를 맞바꿈
            array[j-1],array[j] = array[j],array[j-1]
            
        else : # 본인 미만으로 더 큰수가 없다면 루프를 탈출한다
            break

# 삽입정렬의 시간복잡도는 O(N^2)이다
print(array)
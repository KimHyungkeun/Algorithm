n, m = map(int, input().split()) # n,m 입력
array = list(map(int, input().split())) # 수 입력

array.sort(reverse=True) # 최댓값부터 구하기 위해, 역정렬 시행
maximum = 0

for i in range(0, len(array)-2) :
    for j in range(i+1, len(array)-1) :
        for k in range(j+1, len(array)) :
            if array[i] + array[j] + array[k] <= m and array[i] + array[j] + array[k] > maximum:
                maximum = array[i] + array[j] + array[k] # m 이하면서, 그 중 최대값인것을 구한다.

print(maximum)

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        # 해당 행의 결과값을 담을 임시 리스트
        tmp = []
        # print(arr1[i])
        for j in range(len(arr2[0])) :
            total = 0
            for k in range(len(arr2)) :
                # arr1의 [행][열] * arr1 [열][행] 순으로 곱한 후, total에 누적시킨다
                total += (arr1[i][k] * arr2[k][j])
            tmp.append(total)
        
        # 모든 결과가 나오면 answer에 붙인다
        answer.append(tmp)

    # print(answer) 
    return answer

# arr1 = [[1,4],[3,2],[4,1]]
# arr2 = [[3,3],[3,3]]
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]

solution(arr1, arr2)
# Complete the cutTheSticks function below.
def cutTheSticks(arr):

    # 스틱 크기별로 내림차순(원활한 pop을 위해 일부로 내림차순 정렬함)
    arr.sort(reverse=True)
    answer = []
    
    while arr :
        length = len(arr)
        # 현재 arr의 길이를 answer에 넣는다
        answer.append(length)

        # 현재 arr중에서 가장 길이가 짧은 스틱을 minimum에 넣는다
        minimum = arr[-1]

        # 현 arr에 담긴 각각의 스틱을 minimum 길이만큼 전부 제외시킨다
        for i in range(length) :
            arr[i] -= minimum
        
        # 모두 잘려나가 0이된 스틱은 arr배열에서 제외시킨다
        while 0 in arr :
            arr.pop()
    
    # 위 과정을 반복하며 남은 스틱의 길이들을 answer 배열에 넣는다
    return answer
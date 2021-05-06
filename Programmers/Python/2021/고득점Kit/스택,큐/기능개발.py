def solution(progresses, speeds):
    answer = []
    cnt = 0

    while progresses : # 남은 작업이 없을때까지 계속 반복

        for i in range(len(progresses)) :
            if progresses[i] != 100 : # 작업량이 100이 되면 완료된다
                progresses[i] += speeds[i] # 해당 작업의 하루 스피드만큼 작업량을 올린다
        
        # print(progresses)
        while progresses and progresses[0] >= 100 :
            progresses.pop(0) # 작업이 완료되면 progress리스트에서 해당 작업을 뺀다
            speeds.pop(0) # 그에 대응하는 스피드 리스트도 같이 제거한다
            cnt += 1
        
        if cnt != 0 :
            answer.append(cnt) # 그날 진행했던 배포갯수를 넣는다
            cnt = 0

    # print(answer)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1,1,1,1,1,1]
solution(progresses, speeds)
# Complete the workbook function below.
def workbook(n, k, arr):
    
    # 챕터 확인
    chapter = []

    # 챕터에는 총 n개의 챕터가 있다
    for i in range(n) :
        tmp = []
        # i번째에 적힌 수가 있을때, 1 ~ arr[i]를 k페이지 씩 나눠서 담는다
        for j in range(1, arr[i]+1) :
            if len(tmp) == k :
                chapter.append(tmp)
                tmp = []
            tmp.append(j)
        chapter.append(tmp)
    
    cnt = 0
    # 현 cnt 카운트 횟수가, 현재 챕터페이지 내에 들어있다면 cnt를 증가시킨다
    for i in range(len(chapter)) :
        if i+1 in chapter[i] :
            cnt += 1
    
    return cnt
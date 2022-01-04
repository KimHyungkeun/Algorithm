# 시간 초과 : 50점
def solution(n, left, right):
    ans = []
    blank = []
    
    cnt = -1
    flag = False
    for i in range(n) :
        for j in range(n) :
            if j <= i :
                blank.append(i+1)
            else :
                blank.append(j+1)
            
            cnt += 1
            if cnt >= left :
                ans.append(blank[-1])
            if cnt == right :
                flag = True
                break
                
        if flag :
            break
    
    # print(blank)
    return ans

# 정답
def solution(n, left, right):
    ans = []
    
    # i번째 값을 n으로 나눈 몫과 나머지를 비교해서 그 중, 큰 것을 값으로 넣는다
    for i in range(left, right+1) :
        ans.append(max(i // n, i % n) + 1)

    return ans

# 참고 : https://sangsangss.tistory.com/197
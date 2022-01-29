# 시간초과
def solution(n):
    total = 1
    nums = [i for i in range(1,n)]
    idx = 1
    
    while idx != n :
        for i in range(n - idx) :
            if sum(nums[i:i+idx]) == n :
                total += 1
                break
            if sum(nums[i:i+idx]) > n :
                break
                
        idx += 1
    return total

# 정답 : https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84
def solution(n):
    cnt = 0
    nums = [i for i in range(1,n)]
    
    for i in range(1, n+1) :
        total = 0
        for j in range(i, n+1) :
            total += j
            
            if total == n :
                cnt += 1
                break
            
            if total > n :
                break
    
    
    return cnt

n = 15
result = solution(n)
print(result)
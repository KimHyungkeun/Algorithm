# num을 이진수로 바꿨을때, 그중 1이 등장하는 갯수를 센다
def onecount_bin_base(num) :
    cnt_one = 0
    while num != 0 :
        # num을 2로 계속 나누었을때, 나머지가 1인것들만 카운트한다
        if num % 2 == 1 :
            cnt_one += 1
        num //= 2
    
    # 총 카운트한 1의 갯수를 리턴한다
    return cnt_one

def solution(n):
    answer = n
    
    # n을 이진수로 바꿨을때, 1이 나오는 갯수를 센다
    cnt_one = 0
    while answer != 0 :
        # n을 2로 계속 나누었을때, 나머지가 1인것들만 카운트한다
        if answer % 2 == 1 :
            cnt_one += 1          
        answer //= 2
        
    for i in range(n+1, 1000000) :
        # n의 이진수에서 1이 등장하는 갯수와 n보다 큰 수의 이진수에서 1이 등장하는 갯수가 같은 것을 골라낸다.
        # n보다 큰 수들 중에서 가장 작은 수가 답이다 
        if cnt_one == onecount_bin_base(i) :
            break
        
    return i
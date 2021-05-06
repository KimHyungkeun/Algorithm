# Complete the triplets function below.
def triplets(a, b, c):
    # 리스트 a,b,c를 각각 집합으로 만든 후 오름차순 정렬
    a = sorted(set(a)) 
    b = sorted(set(b))
    c = sorted(set(c))
    cnt = 0
    
    a_cnt = 0 # a배열에서의 경우의 수
    c_cnt = 0 # c배열에서의 경우의 수
    j = 0 # a의 인덱스 위치
    k = 0 # c의 인덱스 위치
    
    for i in range(len(b)) :

        # b이하가 될 수 있는 a의 경우의 수
        while j < len(a) and a[j] <= b[i] :         
                a_cnt += 1
                j += 1
        
        # b이하가 될 수 있는 c의 경우의 수
        while k < len(c) and c[k] <= b[i] :         
                c_cnt += 1
                k += 1
        
        # a * c가 총 경우의 수이다
        cnt += (a_cnt * c_cnt)
        
    return cnt

# https://www.snoopybox.co.kr/1802
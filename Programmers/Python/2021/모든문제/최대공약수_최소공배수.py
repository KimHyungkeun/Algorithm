# 최대공약수를 구하는 함수(유클리드 호제법)
def gcd(n,m) :
    while m != 0 :
        r = n % m 
        n = m
        m = r
    return n


def solution(n, m):
    answer = []
    # 만약 n보다 m이 크면 두 수를 서로 swap 한다    
    if n < m :
        n,m = m, n
     
    g = gcd(n,m) # 최대공약수
    l = g * (n//g) * (m//g) # 최소공배수
    
    answer = [g,l]
    return answer
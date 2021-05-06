from collections import deque
# 최대공약수를 구하는 함수(유클리드 호제법)
def gcd(n,m) :
    while m != 0 :
        r = n % m 
        n = m
        m = r
    return n


def solution(arr):
    arr.sort()
    q = deque(arr) # 원할한 pop, append를 위해 덱으로 만듦
    
    while len(q) != 1 :
        # 가장 left쪽에 있는 두 수를 뽑아낸다
        n = q.popleft() 
        m = q.popleft()
        
        g = gcd(n,m) # 최대공약수
        l = g * (n//g) * (m//g) # 최소공배수
        
        # 구한 최소공배수를 left쪽에 다시 넣음
        q.appendleft(l)
    
    return q[0]
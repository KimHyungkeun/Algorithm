# 시간초과
from itertools import permutations

def solution(n, k):
    
    
    people = [i for i in range(1, n+1)]
    
    result = list(permutations(people, n))
    result.sort()
    
    answer = list(result[k-1])
    return answer

# 정답풀이
# https://codingspooning.tistory.com/84
from math import factorial
def solution(n, k):
    answer = []
    people = [i for i in range(1, n+1)]
    
    while n != 0 :
        fact = factorial(n-1)
        answer.append(people.pop((k-1) // fact) )
        n -= 1
        k %= fact
        
    return answer
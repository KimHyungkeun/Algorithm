# Complete the lonelyinteger function below.
def lonelyinteger(a):
    # 집합타입의 a를 새로 생성
    set_a = set(a)

    # 각 원소별로 등장횟수를 세어서 만약 한번밖에 등장하지 않으면, 그 수가 unique number이다
    for n in set_a :
        if a.count(n) == 1 :
            return n

# 또다른 답
#!/bin/python3

import sys

def lonely_integer(a):
    res = 0
    for elem in a:
        res ^= elem
    return res
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
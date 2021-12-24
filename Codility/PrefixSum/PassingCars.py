# 50% 정답 : Time Out
def solution(A):
    # write your code in Python 3.6
    zero_idx = []
    for i in range(len(A)) :
        if A[i] == 0 :
            zero_idx.append(i)
    
    total = 0
    for z in zero_idx :
        total += sum(A[z:])
        if total > 1000000000 :
            total = -1
            break

    return total

# 100% 정답
def solution(A):
    # write your code in Python 3.6
    total = 0
    basket = [0,0]

    for a in A :
        if a == 0 :
            basket[0] += 1
            basket[1] = 0
        else :
            basket[1] = 1
            total += (basket[0] * basket[1])
        
        if total > 1000000000 :
            total = -1
            break

    return total
# https://sooho-kim.tistory.com/46?category=874886
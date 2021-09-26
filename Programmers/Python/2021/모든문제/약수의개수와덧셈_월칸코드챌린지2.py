def multiple(num) :
    arr = []
    for i in range(1, num+1) :
        if num % i == 0 :
            arr.append(i)
    
    return len(arr)

def solution(left, right):
    total = 0
    
    for i in range(left, right+1) :
        if multiple(i) % 2 == 0 :
            total += i
        else :
            total -= i
    return total
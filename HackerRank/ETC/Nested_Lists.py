from collections import deque
if __name__ == '__main__':
    result = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append((name, score))
    
    result.sort(key = lambda x : x[1])
    min_num = result[0][1]
    result = deque(result)
    
    while result and result[0][1] == min_num :
        result.popleft()
    
    while result :     
        ans.append(result.popleft())
        
        if len(ans) >= 2:
            if ans[-2][1] != ans[-1][1] :
                ans.pop()
                break
    
    ans.sort(key = lambda x : x[0])
    for a in ans :
        print(a[0])
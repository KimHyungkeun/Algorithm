# 실패 : 런타임 에러
def arrayManipulation(n, queries):
    # Write your code here
    
    arr = {i:0 for i in range(1,n+1)}
    
    # 해당 영역 내에서 q[2]만큼의 값을 누적 시킨다
    for q in queries :
        for i in range(q[0], q[1]+1) :
            arr[i] += q[2]
    

    return max(arr.values())
    
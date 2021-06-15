# 실패 : 런타임 에러
# def arrayManipulation(n, queries):
#     # Write your code here
    
#     arr = {i:0 for i in range(1,n+1)}
    
#     # 해당 영역 내에서 q[2]만큼의 값을 누적 시킨다
#     for q in queries :
#         for i in range(q[0], q[1]+1) :
#             arr[i] += q[2]
    

#     return max(arr.values())


# 정답코드
def arrayManipulation(n, queries):
    # Write your code here
    
    arr = [0]*n
    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] != len(arr):
            arr[q[1]] -= q[2]
        
    # print(arr)
    maxval = 0
    itt = 0
    
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt

    return maxval

# https://sites.northwestern.edu/acids/2018/11/12/solution-hackerrank-array-manipulation/

n = 86400
# queries = [[1,5,3],[4,8,7],[6,9,1]]
queries = [[1,86400,1]] * 86400
# queries = [[1,10,1]] * 10
result = arrayManipulation(n, queries)
print(result)


# 정답 참고할만한 예제
# def arrayManipulation(n, queries):
#     # Write your code here
    
#     arr = [0]*n
#     for q in queries:
#         arr[q[0] - 1] += q[2]
#         if q[1] != len(arr):
#             arr[q[1]] -= q[2]
        
#     # print(arr)
#     maxval = 0
#     itt = 0
    
#     for q in arr:
#         itt += q
#         if itt > maxval:
#             maxval = itt

#     print(arr[:10])
#     idx = arr.index(maxval)
    
#     idx += 1
#     cnt = 1
#     while idx < len(arr) and arr[idx] == 0 :
#         cnt += 1
#         idx += 1
#     return cnt
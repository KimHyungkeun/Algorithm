# Complete the balancedSums function below.
def balancedSums(arr):
    
    left_sum = 0 # 왼쪽 파트의 모든 합
    right_sum = sum(arr) # 오른쪽 파트의 모든 합
    
    for i in range(len(arr)) :
        right_sum -= arr[i] # right_sum에서 배열의 해당순서의 원소를 제거한다 
        if left_sum == right_sum : # 만약 두 합이 같다면 YES를 리턴한다
            return "YES"
        left_sum += arr[i] # 그렇지 않다면 left_sum에 해당순서의 원소를 합한다
    
    return "NO" # 모두 탐색했는데도 원하는 결과가 나오지 않는다면 NO를 리턴

# ----------------------------------------------------------------
# https://codereview.stackexchange.com/questions/133850/hackerrank-sherlock-and-array

# 실패 : 시간 초과
# # Complete the balancedSums function below.
# def balancedSums(arr):
#     result = "NO"
#     for i in range(len(arr)) :
#         left = 0
#         right = 0
#         if i == 0 :
#             left = 0
#             right = sum(arr[i+1:])
        
#         elif i == len(arr)-1 :
#             left = sum(arr[:i])
#             right = 0
        
#         else :
#             left = sum(arr[:i])
#             right = sum(arr[i+1:])
        
#         if left == right :
#             result = "YES"
#             break
 
#     return result
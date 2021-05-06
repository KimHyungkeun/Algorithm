# 시간초과 O(N+M)
# def solution(N, A):

#     # write your code in Python 3.6
#     counter = [0] * N
#     length = len(A)
#     maximum = 0

#     for k in A :
#         if k <= N :
#             # 만약 A의 원소 k가 N이하의 수라면
#             counter[k-1] += 1 # k번째 위치의 카운터를 1증가시킨다
#             if counter[k-1] > maximum : # 만약 현재의 maximum보다 크다면, 새로운 최대값으로 갱신
#                 maximum = counter[k-1]

#         else :
#             # 만약 k가 N보다 크다면, counter 전체를 모두 최댓값으로 만든다
#             counter = [maximum] * N

#     # print(counter) 
#     return counter


def solution(N, A):
    # write your code in Python 3.6

    # 1부터 N까지의 빈도수를 구한다
    counter = {i:0 for i in range(1, N+1)}
    # print(counter)

    max_sum = 0 # 최댓값들의 합을 누적함
    max_num = 0 # 현재 차례에서의 최댓값
    for k in A :
        # 만약 A[k]가 N+1과 같다면, 현재의 max_num을 max_sum에 누적시킨다
        if k == N+1 :
            max_sum += max_num 
            counter = {} # 카운터 dict는 다시 초기화시킨다
            max_num = 0 # 현재의 max_num도 다시 0으로 초기화한다
        else :
            # k가 counter내에 없다면 새로 추가한다
            if counter[k] is None:
                counter[k] = 1
            # 이미 존재한다면 빈도수를 1 늘린다
            else :
                counter[k] += 1
            
            # 현재 차례에서의 최대값을 구한다
            max_num = max(max_num, counter[k])

    # 현재까지 쌓인 max_num을 기준으로 N개의 원소를 가지는 리스트를 만든다
    answer = [max_sum] * N
    # print(answer)
    
    # counter 리스트에 담긴 위치들을 알아서 찾아서, val(빈도수)를 더한다
    for key,val in counter.items() :
        answer[key-1] += val
    return answer

# 참고 https://choichumji.tistory.com/89
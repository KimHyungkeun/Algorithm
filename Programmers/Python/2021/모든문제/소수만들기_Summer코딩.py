from itertools import combinations
def solution(nums):
    answer = 0
    b = sum(nums)
    boolean = [False, False] + [True]*(b-1) # 1,2는 소수이므로 False로 지정하고 나머지는 True로 임시 셋팅한다
    primes = []

    for i in range(2, b+1) :
        if boolean[i] : # 해당 수가 소수일때만 prime 리스트에 추가시킨다.
            primes.append(i)
        for j in range(2*i, b+1, i) : # 해당 배수에 포함하는 수들은 모두 False로 만든다.
            boolean[j] = False
    
    # 배열 nums에서 3개를 무작위로 고른다
    arr = list(combinations(nums, 3))
    result = []

    # 무작위로 고른 3개의 수를 모은 경우들의 배열에서, 각 배열들의 합을 구해 result에 넣는다
    for n in arr :
        result.append(sum(n))

    for r in result :
        # 만약 r이 소수라면 카운트를 증가 시킨다
        if r in primes :
            answer += 1
    
    # print(answer)
    return answer

# nums = [1,2,3,4]
nums = [1,2,7,6,4]
solution(nums)
from itertools import permutations

def eratos (b): 
    boolean = [False, False] + [True]*(b-1) # 1,2는 소수이므로 False로 지정하고 나머지는 True로 임시 셋팅한다
    primes = []

    # print(boolean)
    for i in range(2, b+1) :
        if boolean[i] : # 해당 수가 소수일때만 prime 리스트에 추가시킨다.
            primes.append(i)
        for j in range(2*i, b+1, i) : # 해당 배수에 포함하는 수들은 모두 False로 만든다.
            boolean[j] = False

    return boolean


def solution(numbers):
    
    nums = list(numbers) # 숫자들을 리스트 변환
    nums.sort(reverse=True) # 내림차순 정렬(가장 최댓값까지의 모든 소수를 구하기 위함)

    all_prime = ''.join(nums) # 최댓값 까지의 소수를 구함
    boolean = eratos(int(all_prime))
    # print(primes)
    answer = 0

    for i in range(1, len(numbers)+1) :
        result = list(permutations(nums, i)) # 숫자들 중 i개를 뽑음
        # print(result)
        for j in range(len(result)) :
            prime = ''.join(result[j]) # i개를 뽑아 숫자를 만든다
            if boolean[int(prime)] : # 만약 해당 숫자가 소수라면 answer를 하나 늘린다
                answer += 1
                boolean[int(prime)] = False # 중복을 피하기위해 한번 탐색한 숫자는 False로 처리
    
    # print(answer)
    return answer

numbers = "011"
solution(numbers)
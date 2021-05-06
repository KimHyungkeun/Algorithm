import sys

n, k = map(int, sys.stdin.readline().split()) # 2 ~ n까지의 수, k 번째 지워지는 수

numbers = [] # 2 ~ n 까지 오름차순으로 나열
is_prime = [True]*(n-2+1) # 소수판별을 위해 numbers 길이에 맞게 배열설정

for i in range(2, n+1) :
    numbers.append(i)

count = 0 # 몇번재 지워졌는지 카운트
erase_num = 0 # k번째를 만나면, 그 k번째에 해당하는 수를 저장
for i in range(n-2+1) :
    if is_prime[i] : # 만약 해당 수가 True로 되어있으면
        for j in range(i, n-2+1, numbers[i]) : # 가장 작은 수를 기점으로, i의 배수들을 모두 False로 만든다
            if not is_prime[j] : # 이미 False라면 넘어간다
                continue
            else :
                is_prime[j] = False
                count += 1 # 몇번째로 지워졌는지 카운트한다
                if count == k : # k번째에 해당
                    erase_num = j+2 # k번째에 해당하는 수를 찾음. +2를 하는 이유는, 인덱스는 0부터 시작하지만 위 배열은 2부터 시작하므로 +2를 해준다

print(erase_num)

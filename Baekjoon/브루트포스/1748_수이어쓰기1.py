n = input()

length = len(n) # 해당 숫자의 자리수
number = int(n) # 입력한 숫자를 int형으로 저장
answer = 0 # 총 자리수

i = 0
while i < length-1 :
    i += 1
    answer += ( 10 ** i - 10 ** (i-1) ) * i # (10^n - 10^(n-1)) * n , n은 현 수들의 자릿수 범위
    # print(answer)
    

answer += (number - 10**i + 1) * (i+1)

print(answer)
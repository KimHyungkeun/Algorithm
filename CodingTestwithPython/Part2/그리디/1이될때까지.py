import sys

# n,k 입력
n, k = map(int, sys.stdin.readline().split())

# 연산 횟수
cnt = 0
while n != 1 :
    # n과 k가 서로 배수 관계가 아니면 n에서 1을 뺀다
    if n % k != 0 or k == 1:
        n -= 1
    
    # 만약 배수관계라면 n을 k로 나누다
    else :
        n /= k
    
    # 횟수증가
    cnt += 1

print(cnt)

# ---------------------------------------------------------------------------
import sys

# n,k 입력
n, k = map(int, sys.stdin.readline().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
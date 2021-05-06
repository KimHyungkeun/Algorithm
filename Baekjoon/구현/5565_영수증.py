import sys

origin = int(sys.stdin.readline()) # 책 10권의 가격

total = 0
for _ in range(9) : # 가격확인 가능한 9개의 책들
    num = int(sys.stdin.readline())
    total += num

print(origin - total) # 책 10권 가격에서 확인가능한 9권의 가격합을 뺀다
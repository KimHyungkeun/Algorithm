import sys

# 최솟값을 위해서는 곱했을때의 결과가 최대한 작은값들이 나와야 한다

# 길이가 n개
n = int(sys.stdin.readline())

# a 배열과 b 배열을 입력
a = list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True) # 우선순위대로 뽑아내기위해 내림차순 정렬한다
b = list(map(int, sys.stdin.readline().split()))

# 새로이 순서가 재정의될 배열 a
new_a = [0] * n
# 해당 요소의 우선순위까지 표시하기 위한 배열 b
new_b = []

# b배열에 우선순위를 매기고, 내림차순으로 정렬한다
for i in range(n) :
    new_b.append((b[i], i))
new_b.sort(reverse=True)

# 해당 위치의 요소와 곱하게될 적절한 a가 배치된다
for i in range(n) :
    new_a[new_b[i][1]] = a.pop()

# a와 b를 곱해서 나온 값들을 모두 더한다 
total = 0
for i in range(n) :
    total += (new_a[i] * b[i])

print(total)
# print(new_a)
# print(b)


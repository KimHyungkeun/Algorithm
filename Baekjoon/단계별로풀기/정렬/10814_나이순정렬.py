import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n) :
    age, name = sys.stdin.readline().split()
    # i는 가입 순서를 뜻한다
    arr.append((int(age), name, i))

# 가입 순서별로 먼저 오름차순 정렬 한다
sort_arr = sorted(arr, key = lambda x : x[2])
# 그 후, 나이가 어린순서부터 정렬한다
sort_arr = sorted(sort_arr, key = lambda x : x[0])

for a in sort_arr :
    print(a[0], a[1])
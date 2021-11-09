import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    arr.append(word)

# 중복된 단어의 경우, 한번만 출력되도록 하기위해 집합으로 바꿈
arr = list(set(arr))

# 사전순으로 먼저 정렬
sort_arr = sorted(arr)

# 그 후, 단어 길이별로 정렬
sort_arr = sorted(sort_arr, key = lambda x :len(x))

for a in sort_arr :
    print(a)
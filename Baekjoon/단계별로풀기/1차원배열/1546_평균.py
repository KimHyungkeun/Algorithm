import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
max_score = max(arr)

new_arr = []
for a in arr :
    new_arr.append((a/max_score) * 100)

print(sum(new_arr) / len(new_arr))
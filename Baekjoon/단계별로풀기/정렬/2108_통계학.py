import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n) :
    num = int(sys.stdin.readline())
    arr.append(num)

avg = sum(arr) // n

sort_arr = sorted(arr)
mid = len(sort_arr) // 2
arr_mid = sort_arr[mid]

max_dict = {}
set_arr = list(set(arr))
for s in set_arr :
    max_dict[s] = arr.count(s)
max_val = max(max_dict.values())
max_result = []
# print(max_dict)
for key,val in max_dict.items() :
    if val == max_val :
        max_result.append(key)

if len(max_result) >= 2 :
    max_result.sort()
    max_cnt = max_result[1]

else :
    max_cnt = max_result[0]


ranges = sort_arr[-1] - sort_arr[0]

print(avg)
print(arr_mid)
print(max_cnt)
print(ranges)
import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n) :
    num = int(sys.stdin.readline())
    arr.append(num)

sort_arr = sorted(arr)
max_dict = {}
for s in sort_arr :
    if s not in max_dict :
        max_dict[s] = 1
    else :
        max_dict[s] += 1
sorted_max_dict = sorted(max_dict.items(), key = lambda x : x[1], reverse=True)

# 1. 산술평균
avg = round(sum(arr) / n)

# 2. 중앙값
mid = len(sort_arr) // 2
arr_mid = sort_arr[mid]

# 3. 최빈값
max_result = []
# print(sorted_max_dict)
for key,val in sorted_max_dict :
    if not max_result :
        max_result.append((key,val))
    else :
        if val == max_result[-1][1] :
            max_result.append((key,val))
            break
        else :
            break

if len(max_result) == 2 :
    max_result.sort(key = lambda x : x[0])
    max_cnt = max_result[1][0]

else :
    max_cnt = max_result[0][0]

# 4. 범위
ranges = sort_arr[-1] - sort_arr[0]

print(avg)
print(arr_mid)
print(max_cnt)
print(ranges)
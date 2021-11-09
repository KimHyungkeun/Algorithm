import sys

n = int(sys.stdin.readline())
num_dict = {}
max_num = 0
for _ in range(n) :
    num = int(sys.stdin.readline())
    max_num = max(max_num, num)
    if num in num_dict :
        num_dict[num] += 1
    else :
        num_dict[num] = 1

for i in range(1, max_num + 1) :
    if i not in num_dict :
        continue
    else :
        for j in range(num_dict[i]) :
            print(i)
            


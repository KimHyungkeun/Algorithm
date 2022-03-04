# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
import sys

nums = sys.stdin.readline().rstrip()
result = []
cnt = 1
for i in range(len(nums)) :
    if i == 0 :
        continue
    elif nums[i-1] != nums[i] :
        result.append((cnt, int(nums[i-1])))
        cnt = 1
    else :
        cnt += 1
    
if i == len(nums)-1 :
    result.append((cnt, int(nums[i])))

for r in result :
    print(r,end=' ')
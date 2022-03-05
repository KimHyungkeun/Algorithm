# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import combinations
n = int(sys.stdin.readline())
words = list(sys.stdin.readline().split())
k = int(sys.stdin.readline())

cnt = 0
result = list(combinations(words, k))
for r in result :
    if 'a' in r :
        cnt += 1

ans = cnt / len(result)
print(ans)
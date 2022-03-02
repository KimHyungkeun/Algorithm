# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
import sys

word, num = sys.stdin.readline().split()
word = list(word)
num = int(num)
word.sort()

ans = []
for i in range(1, num+1) :
    result = list(combinations(word, i)) 
    for r in result :
        ans.append(''.join(r))

for a in ans:
    print(a)
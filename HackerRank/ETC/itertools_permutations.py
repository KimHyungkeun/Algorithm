# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
import sys

word, num = sys.stdin.readline().split()
num = int(num)
word = list(word)

result = list(permutations(word, num))
result.sort()
for r in result :
    print(''.join(r))
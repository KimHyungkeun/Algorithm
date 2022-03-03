# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
import sys

word, num = sys.stdin.readline().split()
word = list(word)
num = int(num)
word.sort()

result = list(combinations_with_replacement(word, num))
for r in result :
    print(''.join(r))
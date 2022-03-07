# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys

x = int(sys.stdin.readline())
shoes = list(map(int, sys.stdin.readline().split()))
shoes_list = Counter(shoes)


n = int(sys.stdin.readline())
total = 0
for _ in range(n) :
    shoes_type, cost = map(int, sys.stdin.readline().split())
    if shoes_list[shoes_type] != 0 :
        shoes_list[shoes_type] -= 1
        total += cost

print(total)
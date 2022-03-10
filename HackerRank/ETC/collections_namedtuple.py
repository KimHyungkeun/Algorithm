# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
import sys

n = int(sys.stdin.readline())
col = list(sys.stdin.readline().split())

total = 0
for _ in range(n) :
    Column = namedtuple('Column',' '.join(col))
    field1, field2, field3, field4 = sys.stdin.readline().split()
    Column = Column(field1, field2, field3, field4)
    total += int(Column.MARKS)

print(total / n)

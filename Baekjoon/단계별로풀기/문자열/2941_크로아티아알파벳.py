import sys

string = sys.stdin.readline().rstrip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia :
    if c in string :
        string = string.replace(c, '0')

print(len(string))

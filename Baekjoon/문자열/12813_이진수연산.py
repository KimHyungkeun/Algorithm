import sys

a = sys.stdin.readline().rstrip() 
b = sys.stdin.readline().rstrip()

# AND
for i in range(len(a)) :
    if a[i] == '1' and b[i] == '1' :
        print('1',end='')
    else :
        print('0',end='')
print()

# OR
for i in range(len(a)) :
    if a[i] == '0' and b[i] == '0' :
        print('0',end='')
    else :
        print('1',end='')
print()

# NOT
for i in range(len(a)) :
    if a[i] != b[i] :
        print('1',end='')
    else :
        print('0',end='')
print()

# ~A
for i in range(len(a)) :
    if a[i] == '1' :
        print('0',end='')
    else :
        print('1',end='')
print()

# ~B
for i in range(len(a)) :
    if b[i] == '1' :
        print('0',end='')
    else :
        print('1',end='')
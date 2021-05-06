import sys

def hanoi(n, frm , otr ,to) :
    if n == 1 :
        print(frm,to)
    else :
        hanoi(n-1,frm,to,otr)
        print(frm,to)
        hanoi(n-1,otr,frm,to)

n = int(sys.stdin.readline())
print((2**n)-1)
hanoi(n,1,2,3)
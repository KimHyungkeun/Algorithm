import sys

n = sys.stdin.readline().rstrip()
start = n
arr = [0,0]

round = 0
while True :
    if round == 0 and len(n) == 1 :
        print(round+1)
        break
    
    if round == 0 :
        arr[0] = int(n[0])
        arr[1] = int(n[1])
        n = str(int(n[0]) + int(n[1]))
            
         
    else :
        if len(n) == 1 :
            backup = int(n[0])
            n = str(arr[1]) + n[0]

            arr[0] = int(n[0])
            arr[1] = int(n[1])

        else :
            
            n = str(arr[0] + arr[1])
            backup = int(n[-1])

            arr[0] = arr[1]
            arr[1] = backup

            
    
    # print(n)
    if int(str(arr[0])+str(arr[1])) == int(start) and round > 0:
        print(round)
        break
    
    round += 1






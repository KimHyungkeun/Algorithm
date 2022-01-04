# 211231 : 30점
import sys
digits = {"0" : [1,1,1,0,1,1,1],
          "1" : [0,0,1,0,0,1,0],
          "2" : [1,0,1,1,1,0,1],
          "3" : [1,0,1,1,0,1,1],
          "4" : [0,1,1,1,0,1,0],
          "5" : [1,1,0,1,0,1,1],
          "6" : [1,1,0,1,1,1,1],
          "7" : [1,1,1,0,0,1,0],
          "8" : [1,1,1,1,1,1,1],
          "9" : [1,1,1,1,0,1,1]
          }

n = int(sys.stdin.readline())
for _ in range(n) :
    before, after = sys.stdin.readline().split()

    if len(before) == len(after) :
        for i in range(len(before)) :
            cnt = 0
            for j in range(7) :
                if digits[before[i]][j] != digits[after[i]][j] :
                    cnt += 1
        print(cnt)
    
    elif len(before) > len(after) :
        cnt = 0
        start = 0
        while len(before) - start != len(after) :
            cnt += sum(digits[before[start]])
            start += 1 
        
        for i in range(start, len(before)) :
            for j in range(7) :
                if digits[before[i]][j] != digits[after[i-start]][j] :
                    cnt += 1

        print(cnt) 
        
    else :
        cnt = 0
        start = 0
        while len(after) - start != len(before) :
            cnt += sum(digits[after[start]])
            start += 1 
        
        for i in range(start, len(after)) :
            for j in range(7) :
                if digits[before[i-start]][j] != digits[after[i]][j] :
                    cnt += 1
            # print(i,before[i-start],after[i],"mid result :",cnt)

        print(cnt) 

# ------------------------------------------------------------------------------
# 220102 풀이
import sys
digits = {"0" : [1,1,1,0,1,1,1],
          "1" : [0,0,1,0,0,1,0],
          "2" : [1,0,1,1,1,0,1],
          "3" : [1,0,1,1,0,1,1],
          "4" : [0,1,1,1,0,1,0],
          "5" : [1,1,0,1,0,1,1],
          "6" : [1,1,0,1,1,1,1],
          "7" : [1,1,1,0,0,1,0],
          "8" : [1,1,1,1,1,1,1],
          "9" : [1,1,1,1,0,1,1],
          " " : [0,0,0,0,0,0,0]
          }

n = int(sys.stdin.readline())
for _ in range(n) :
    before, after = sys.stdin.readline().split()

    before = (5-len(before)) * ' ' + before
    after = (5-len(after)) * ' ' + after

    cnt = 0
    for i in range(5) :
        for j in range(7) :
            if digits[before[i]][j] != digits[after[i]][j] :
                cnt += 1 
    
    print(cnt)

# -------------------------------------------------------------
# 220104 풀이
import sys
digits = {"0" : [1,1,1,0,1,1,1],
          "1" : [0,0,1,0,0,1,0],
          "2" : [1,0,1,1,1,0,1],
          "3" : [1,0,1,1,0,1,1],
          "4" : [0,1,1,1,0,1,0],
          "5" : [1,1,0,1,0,1,1],
          "6" : [1,1,0,1,1,1,1],
          "7" : [1,1,1,0,0,1,0],
          "8" : [1,1,1,1,1,1,1],
          "9" : [1,1,1,1,0,1,1],
          " " : [0,0,0,0,0,0,0]
          }

n = int(sys.stdin.readline())
for _ in range(n) :
    before, after = sys.stdin.readline().split()
    before = ' ' * (5-len(before)) + before
    after = ' ' * (5-len(after)) + after

    cnt = 0
    for i in range(5) :
        for j in range(7) :
            if digits[before[i]][j] != digits[after[i]][j] :
                cnt += 1
    
    print(cnt)
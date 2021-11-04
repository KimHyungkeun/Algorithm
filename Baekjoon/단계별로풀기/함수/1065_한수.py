import sys

def d(n) :
    # 한자리 수라면 한수가 된다
    if len(str(n)) == 1 :
        return True
    
    else :
        list_num = list(str(n))
        # 각 자릿수별 차를 arr 배열에 담는다
        arr = []
        for i in range(len(list_num)-1) :
            arr.append(int(list_num[i]) - int(list_num[i+1]))
        
        # 자릿수별 차가 일정하면 한수이다
        if len(set(arr)) == 1 :
            return True
        
        # 자릿수별 차이가 하나라도 다르다면 한수가 아니다.
        else :
            return False


n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n+1) :
    if d(i) :
        cnt += 1

print(cnt)


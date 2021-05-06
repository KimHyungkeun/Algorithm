# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    
    cnt = 0
    for n in range(i,j+1) :
        
        int_num = n # 정수 n을 설정
        # 정수 n의 자리수 순서를 바꾸기위해 임의로 리스트형으로 바꾼후, 
        # reverse 함수로 순서를 거꾸로하여 다시 재 join 시켜 정수형으로 바꾼다
        str_num = str(n) 
        str_num = list(str_num)
        str_num.reverse()
        rev_num = ''.join(str_num)
        rev_num = int(rev_num)
        
        # int_num과 순서가 거꾸로된 rev_num의 절대값 차를 구하여, k에 나누어떨어진다면 카운트를 올린다
        ans = abs(int_num-rev_num)
        if ans % k == 0 :
            cnt += 1
    
    return cnt
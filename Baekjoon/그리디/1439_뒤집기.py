s = list(input())

# 0과 1중 선택하여, 뒤집기를 시전했을때 경우의 수가 더 적은것을 고름
def reverse_count(maximum_num) :
    i = 0
    # 뒤집기를 시전한 횟수
    cnt = 0
    # 연속된 수가 나올때까지는 combo를 유지
    combo = 0
    while i < len(s) :
        # 지정한 기준 수와 틀린 수가 나올 경우, 그 수가 지속되는만큼 콤보를 유지 
        if s[i] != maximum_num :
            combo = 1
            i += 1
        
        # 지정한 기준 수와 맞을 경우, 시전횟수를 증가. 쌓인 연속콤보는 초기화
        else :
            cnt += combo
            combo = 0
            i += 1

    # 미처 계산치 못한 횟수를 마저 추가하고, 값 리턴
    cnt += combo
    return cnt

# 0과 1중 뒤집기 시전시, 가장 적은 횟수가 나오는 경우를 택1
if reverse_count('0') > reverse_count('1') :
    result =  reverse_count('1')
   
else :
    result =  reverse_count('0')

print(result)
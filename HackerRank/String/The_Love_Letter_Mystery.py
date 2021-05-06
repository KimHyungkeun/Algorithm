# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    
    # 현재의 문자열이 팰린드롬이 되어야 한다
    
    cnt = 0 # 팰린드롬 교정을 위해 단어를 바꾼 횟수
    mid = len(s) // 2 # 대칭점 선정을 위해 mid를 설정한다
    
    # 문자열 길이가 홀수일 경우
    if len(s) % 2 != 0 :       
        # 끝지점 end를 설정한다
        end = len(s)-1
        while mid < end :
            # 해당 인덱스의 대칭점이 되는곳을 찾아서, 아스키코드 간의 격차를 구한다
            cnt += abs(ord(s[end]) - ord(s[len(s)-1-end]))
            end -= 1
    
    # 문자열 길이가 짝수일 경우
    else :
        # 끝지점 end를 설정한다
        end = len(s)-1
        while mid <= end :
            # 해당 인덱스의 대칭점이 되는곳을 찾아서, 아스키코드 간의 격차를 구한다
            cnt += abs(ord(s[end]) - ord(s[len(s)-1-end]))
            end -= 1
    
    return cnt
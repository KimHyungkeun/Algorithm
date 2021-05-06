# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    
    cnt = 0
    # 만약 i와 i+1번째의 철자가 서로 같다면 cnt를 증가한다
    # 문자열은 A,B로만 구성되어야하며, 바로 다음글자가 이전글자와 다른 것이어야 하기 때문이다 
    for i in range(len(s)-1) :
        if s[i] == s[i+1] :
            cnt += 1
    return cnt
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s2 = list(s2) # 스펠링 하나하나를 확인하기위해 리스트로 바꿈
    cnt = 0 # s2의 스펠링이 s1의 substring에 하나라도 포함되는지 카운트하기위한 변수
    for w in s2 :
        if w in s1 : # 만약 s2의 철자가 s1에도 포함된다면 갯수 증가
            cnt += 1
    
    # 하나라도 s1과 s2의 철자가 겹치는게 있다면 YES, 아니면 NO
    if cnt >= 1 :
        return "YES"
    
    else :
        return "NO"
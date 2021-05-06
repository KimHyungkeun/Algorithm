# Complete the camelcase function below.
def camelcase(s):
    
    cnt = 1
    # 대문자를 발견할때마다 cnt를 늘린다.(새로운 대문자 등장이 곧 새로운 단어의 시작이므로)
    for w in s :
        if "A" <= w <= "Z" :
            cnt += 1
    
    return cnt
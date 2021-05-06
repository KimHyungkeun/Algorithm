# Complete the marsExploration function below.
def marsExploration(s):
    
    # SOS 문구
    SOS = "SOS"
    cnt = 0

    # 수신되는 메시지를 비교하여, SOS철자와 한글자씩 다를때마다 cnt를 늘린다
    for i in range(0, len(s), 3) :
        tmp = s[i:i+3]
        for j in range(len(tmp)) :
            if tmp[j] != SOS[j] :
                cnt += 1
    
    return cnt
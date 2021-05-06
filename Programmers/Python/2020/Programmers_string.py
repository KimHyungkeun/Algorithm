def solution(s):
    
    # 길이가 4나 6이어야한다
    if len(s) == 4 or len(s) == 6 :
        # 오로지 숫자로만 있어야한다
        for w in s :
            if (ord('a') <= ord(w) <= ord('z')) or (ord('A') <= ord(w) <= ord('A')) :
                return False
    else :
        return False

    
    return True
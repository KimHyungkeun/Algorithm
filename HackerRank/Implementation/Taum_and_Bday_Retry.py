def taumBday(b, w, bc, wc, z):
    # Write your code here
    answer = 0
    
    # 검은색 가격 + 색깔 교환 비용 < 흰색 가격
    if bc + z < wc :
        answer = b*bc + w*(bc+z)
    
    # 흰색가격 + 색깔 교환 비용 < 검은색 가격
    elif wc + z < bc:
        answer = b*(wc+z) + w*wc
    
    # 흰색가격 + 검은색 가격 < 색깔 교환 비용
    else :
        answer = b*bc + w*wc
    
    return answer

# http://egloos.zum.com/udgrasil/v/2633961
# 최대공약수 구하는 함수
def gcd(a, b) :
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

def solution(w,h):
    answer = 0
    
    total = w * h # 전체 정사각형의 갯수
    
    # 최대공약수를 구하기 위해, w가 더 큰 수로 오도록 한다
    if w < h :
        w, h = h, w
    
    # 최대공약수 구함
    g = gcd(w,h)
    
    # 쓸 수 없는 사각형 갯수 구함
    nonuse = w//g + h//g - 1
    
    # 만약 w,h가 같은 정사각형 모양이라면, w또는 h갯수만큼만 제외한 나머지 사용이 가능
    if w == h :
        answer = total - w
    
    # 그 외에는 nonuse 동안의 값을 제외
    else :
        answer = total - (nonuse * g)
    
    
    return answer
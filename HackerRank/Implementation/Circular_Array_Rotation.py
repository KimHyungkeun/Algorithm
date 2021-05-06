# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # k번 배열을 로테이션 시킨다(top의 요소를 bottom으로 가져온다)
    for _ in range(k) :
        a.insert(0, a.pop())
    
    result = []
    # 로테이션 시킨 배열에 대해서 q번째 요소를 구한다
    for q in queries :
        result.append(a[q])
    
    return result
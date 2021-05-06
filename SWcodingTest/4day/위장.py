def solution(clothes):
    # answer = 0
    cloth_dict = {}

    # 입력된 모든 옷종류의 수를 구한다
    for w in clothes :
        if w[1] in cloth_dict :
            cloth_dict[w[1]] += 1
        else :
            cloth_dict[w[1]] = 1
    
    # 입을수 있는 총 경우는 (옷종류1 + 1) * (옷종류2 + 1) * ... (옷중류n + 1) - 1 이다
    total = 1
    for key,val in cloth_dict.items() :
        total *= (cloth_dict[key] + 1)
    
    total -= 1
    return total
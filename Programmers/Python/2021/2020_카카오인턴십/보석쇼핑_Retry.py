from collections import defaultdict
def solution(gems):
    size = len(set(gems)) # 보석 종류의 갯수
    gem_dict = {gems[0]:1} # 보석 종류를 담기위한 dict 자료형
    tmp = [0, len(gems)-1] # 초기에는 모든 범위로 설정한다

    start = 0 # 시작지점
    end = 0 # 끝지점

    # start와 end 둘다 gems 리스트 범위 내여야한다
    while start < len(gems) and end < len(gems) :
        # 만약 해당 범위내에 모든 보석종류가 다 들어있다면
        if len(gem_dict) == size :
            # 만약 해당 범위가 이전 범위보다도 더 협소한 범위라면 새로 갱신
            if end - start < tmp[1] - tmp[0] :
                tmp = [start, end]
            
            # 어떤 범위를 완전히 벗어나 특정 보석이 보이지 않으면, 그 범위 내에 있던 보석은 사라진다
            if gem_dict[gems[start]] == 1 :
                del gem_dict[gems[start]]

            # 범위가 옮겨질때마다 해당 보석의 빈도수는 감소한다
            else :
                gem_dict[gems[start]] -= 1
            start += 1

        else :
            # 끝 지점을 더 넓혀본다
            end += 1

            # 만약 gems범위 끝까지 탐색했다면 루프문 탈출 
            if end == len(gems) :
                break
            # 이미 존재하는 보석이면 빈도수만 증가시킨다
            if gems[end] in gem_dict.keys() :
                gem_dict[gems[end]] += 1
            # 처음 보는 보석이라면 dict에 추가한다
            else :
                gem_dict[gems[end]] = 1

        # print(start, end, gem_dict)

    # print(tmp)

    # 0부터 시작하는 인덱스이므로, 1씩 더해준다
    return [tmp[0]+1, tmp[1]+1]

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["A","A","B"]
solution(gems)

# https://kdgt-programmer.tistory.com/65
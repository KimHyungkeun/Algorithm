from collections import defaultdict
def solution(gems):
    length = len(gems) # 보석 진열 장 총 길이
    size = len(set(gems)) # 보석 종류들의 갯수
    gem_dict = {gems[0]:1} # 현재 범위 내에서의 보석 종류와 갯수
    tmp = [0, length-1] # 현재의 범위

    left = 0 # 시작점
    right = 0 # 끝점

    # 보석 진열장 범위 내에서의 탐색
    while left < length and right < length :

        # 만약 모든 보석들이 존재할 경우
        if len(gem_dict) == size :
            # 현재 범위가 이전 범위보다도 더 좁은 케이스라면 새로 갱신한다
            if right - left < tmp[1] - tmp[0] :
                tmp = [left, right]

            # left를 옮기기 전에 left위치에 있었던 보석 종류가 1개밖에 없었다면, left위치가 옮겨짐으로써 아예 언급되지 않게된다.
            if gem_dict[gems[left]] == 1 :
                del gem_dict[gems[left]]
            
            # 1개이상 남아있다면, 갯수가 줄어들게 된다
            else :
                gem_dict[gems[left]] -= 1
            
            left += 1
        
        else :
            # right를 한칸 옮긴다
            right += 1

            # 만약, gems 진열장 끝까지 같다면 탐색 종료
            if right == length :
                break
            
            # right위치에 있는 보석이 이미 현재 범위내에 존재한다면, 탐색개수를 늘린다
            if gem_dict.get(gems[right]) :
                gem_dict[gems[right]] += 1
            # 현 범위내에서 새로 발견된 보석이라면, 탐색개수를 1로 설정
            else :
                gem_dict[gems[right]] = 1

            
    # 범위 리턴(인덱스 0부터 시작한 범위이므로, 1씩 더해줌)
    return [tmp[0]+1, tmp[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)

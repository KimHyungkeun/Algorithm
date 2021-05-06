from itertools import permutations
def solution(user_id, banned_id):

    result = []
    for candidate in permutations(user_id, len(banned_id)) :
        # print(list(candidate))
        # 유저ID 갯수 중에서, 불량사용자 ID갯수 만큼 뽑아낼 수 있는 순열들을 구한다
        candidate = list(candidate)

        flag = True
        for i in range (len(banned_id)) :
            # 불량사용자 ID 패턴 길이와 유저ID 패턴길이가 같은것들 위주로 먼저 비교한다
            if len(banned_id[i]) == len(candidate[i]) :
                # 불량사용자 ID 패턴중에 '*'는 그냥 무시하면 되고, 그 외의 문자만 같은지만 비교한다
                for j in range (len(banned_id[i])) :
                    if banned_id[i][j] == '*' :
                        continue
                    if candidate[i][j] != banned_id[i][j] :
                        flag = False
                        break 
            # 길이 조차 다르다면 해당되는 패턴의 유저ID가 아닌 것이다
            else :
                flag = False
                break
        
        # 최종적으로 불량사용자 패턴과 모두 일치하며, 지금까지 담긴 불량사용자 공간에 처음으로 들어갈 유저ID라면 새로 추가한다.
        # ID순서만 다를 뿐, 중복된 내용이 있을 수 있으므로 리스트형태의 candidate를 집합형태로 캐스팅하여 집어 넣는다 
        if flag and set(candidate) not in result :
            result.append(set(candidate))
    

    # 지금 까지 담긴 result 내의 원소 갯수를 값으로 리턴한다
    cnt = len(result)
    print(cnt)   
    return cnt

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id = ["fr*d*", "abc1**"]
# banned_id = ["*rodo", "*rodo", "******"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

solution(user_id, banned_id)

# 참고 : https://codingspooning.tistory.com/85
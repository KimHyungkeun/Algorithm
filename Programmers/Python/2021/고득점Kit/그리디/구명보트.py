# def solution(people, limit) :
#     count = 0

#     # 사람들을 무게별로 정렬
#     people.sort()

#     # 첫번째 사람과, 마지막 사람
#     start = 0
#     end = len(people)-1

#     while start <= end:

#         # 무조건 구명보트에는 1명 이상 태우는 경우가 있으므로, cnt 상승
#         count += 1

#         # 만약 두 사람의 몸무게가 limit 이하라면 무게가 그다음으로 낮은사람과 무거운사람을 비교
#         if people[start] + people[end] <= limit :
#             start += 1
           
#         # 몸무게를 초과한다면, 무거운 사람 1명만 먼저 내보내고 그다음 무거운 사람을 비교
#         end -= 1 
    
#     # 구조횟수
#     return count

# 210302 새 풀이
def solution(people, limit) :
    
    # 몸무게 순서대로 정렬
    people.sort()
    
    # 시작사람과 끝사람을 정함
    start = 0
    end = len(people)-1
    
    cnt = 0
    while start <= end :

        # 만약 두 사람을 태웠을때 limit보다 크다면, end쪽 사람만 태우고 그 다음 무거운 사람을 가리킨다
        if people[start] + people[end] > limit :
            end -= 1
            cnt += 1
        
        # 만약 두 사람 모두 limit 이내라면, start와 end 쪽 사람 둘다 태우고 그 다음의 start와 end쪽 사람을 가리킨다
        else :
            start += 1
            end -= 1
            cnt += 1
    
    # 답 리턴
    return cnt

# people = [70,50,80,50]
people = [70,80,50]
limit = 100
solution(people, limit)
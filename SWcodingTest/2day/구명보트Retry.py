from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    boat = []

    cnt = 0
    while people :

        if not boat :
            boat.append(people.popleft())

        while people and sum(boat) + people[0] <= limit :
            boat.append(people.popleft())
       
        boat = []
        cnt += 1

             
    print(cnt)
    return cnt

people = [50]
limit = 100
solution(people, limit)

# -----------------------------------------------------------------------


# 정답코드 210119
def solution(people, limit) :
    people.sort()

    first = 0
    second = len(people)-1
    count = 0

    while first <= second :
        count += 1
        if people[first] + people[second] <= limit :
            first += 1
        second -= 1
    
    return count

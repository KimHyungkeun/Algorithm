from itertools import product

def solution(word):
    answer = 0
    list1 = ['A','E','I','O','U']
    # list1의 요소를 이용해 중복순열을 발생시킨다. 2~5개까지 
    list2 = list(map(list, product(list1, repeat=2)))
    list3 = list(map(list, product(list1, repeat=3)))
    list4 = list(map(list, product(list1, repeat=4)))
    list5 = list(map(list, product(list1, repeat=5)))
    total_list = list1 + list2 + list3 + list4 + list5

    # 리스트로 정리된 철자 리스트를 하나의 문자열로 정리한다
    for i in range(len(total_list)) :
        total_list[i] = ''.join(total_list[i])
    
    # 문자열 순서대로 정렬
    total_list.sort()
    answer = total_list.index(word) + 1
    return answer

# 참고 : https://velog.io/@guswl8280/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%8C-%EC%82%AC%EC%A0%84-Python
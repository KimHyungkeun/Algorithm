from collections import Counter

# Complete the anagram function below.
def anagram(s):

    # Counter 함수는 문자열에 들어있는 철자 종류와 갯수를 dict 형태로 리턴한다.
    # 해당 dict에 없는 key의 val은 0으로 된다

    # 홀수이면 바꿀수 있는 경우가 없으므로 -1 리턴
    if len(s) % 2 == 1 :
        return -1
    
    res = 0 # 바꿔야하는 문자 갯수
    mid = len(s)//2 # 중간지점을 기준으로 나누기위해, 중간점 설정
    cnt1 = Counter(s[:mid]) # 중간지점 이전까지의 철자종류와 갯수들
    cnt2 = Counter(s[mid:]) # 중가지점 이후까지의 철자종류와 갯수들
    cnt3 = {} # 새로 바꿔져야될 수들
    
    
    for key, val in cnt1.items() :
        cnt3[key] = abs(val - cnt2[key])
        # print(key, cnt2[key], cnt3)
    for key, val in cnt2.items() :
        cnt3[key] = abs(val - cnt1[key])
        # print(key, cnt1[key], cnt3)
    
    for el in cnt3.values() :
        res += el
    
    return res//2
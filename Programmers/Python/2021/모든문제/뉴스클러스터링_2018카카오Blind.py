from itertools import combinations
def solution(str1, str2):
    answer = 0

    # 철자 통일을 위해, 알파벳은 모두 소문자로 바꾸도록 한다
    str1 = str1.lower()
    str2 = str2.lower()
    
    
    combi1 = [] # str1에 대한 알파벳 조합
    combi2 = [] # str2에 대한 알파벳 조합
    # 알파벳 두 쌍으로만 이루어진 조합을 구한다
    for i in range(len(str1)-1) :
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z' :
            combi1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1) :
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i+1] <= 'z' :
            combi2.append(str2[i]+str2[i+1])
    
    # 만약 combi1, combi2가 모두 공집합이면, 공집합에 대한 교집합 합집합이 모두 같으므로 65536을 그대로 반환한다
    if not combi1 and not combi2 :
        answer = 65536
    # combi1이나 combi2중 하나가 비어있다면, 교집합이 0이란 뜻이므로 0을 반환한다
    elif (combi1 and not combi2) or (not combi1 and combi2) :
        answer = 0
    else :        
        # 두 combi1, combi2에 대한 교집합을 구한다
        inter = list(set(combi1) & set(combi2))
        inter_cnt = 0 # 교집합 갯수를 구한다.(중복도 포함하는 집합이므로 원소를 중복해서 셀수도 있다)
        for w in inter :
            cnt1 = 0
            for com1 in combi1 : # combi1에 대해 현재 inter갯수가 몇개인지 구한다
                if com1 == w :
                    cnt1 += 1
            cnt2 = 0
            for com2 in combi2 : # combi2에 대해 현재 inter갯수가 몇개인지 구한다
                if com2 == w :
                    cnt2 += 1
            inter_cnt += min(cnt1, cnt2) # 두 조합에 각각에 대한 inter(교집합) 출현 갯수중에, 최소값이 최종 교집합 갯수가 된다

        union = len(combi1) + len(combi2) - inter_cnt # 합집합은 두 집합의 총 갯수에서 교집합 갯수만큼 제외하면 된다
        answer = int((inter_cnt / union) * 65536)  # 교집합 갯수 / 합집합 갯수 * 65536을 한 후, 정수부분만 골라낸다
        
    return answer
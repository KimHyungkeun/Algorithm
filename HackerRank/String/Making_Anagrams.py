# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):

    # 두 문자열의 공통문자와 갯수를 구해서, s1과 s2의 문자열길이에서 그 갯수만큼 제외하면 사라져야할 문자들의 갯수가 나온다 

    # 철자 하나하나를 다루기위해 각 문자열을 리스트타입으로 변환
    s1 = list(s1)
    s2 = list(s2)
    # 두 문자열의 교집합을 구하고, 두 문자열의 길이의 합을 구한다
    common = set(s1) & set(s2)
    total = len(s1) + len(s2)
    
    # s1에서 등장하는 공통문자의 갯수
    common_spell1 = []
    # s2에서 등장하는 공통문자의 갯수
    common_spell2 = []
    # 위 문자열에서의 공통문자 갯수를 구해서 그 중, 가장 최소값을 최종 리스트에 담으려한다
    last_spell = []
    
    for w in common :
        common_spell1.append((w, s1.count(w)))
        common_spell2.append((w, s2.count(w)))
    
    for i in range(len(common_spell1)) :
        # s1과 s2에서 등장하는 공통문자의 문자 갯수 중, 가장 적게등장하는 쪽을 last_spell 리스트에 넣는다
        if common_spell1[i][1] < common_spell2[i][1] :
            last_spell.append(common_spell1[i])
        else :
            last_spell.append(common_spell2[i])
    
    # 공통적으로 나타나는 문자열을 제거한다
    for w in last_spell :
        # s1, s2에서 동시에 사라지므로, 문자갯수에 X2를 한다
        total -= (2*w[1])
        
    return total
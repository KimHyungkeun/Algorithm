# Complete the pangrams function below.
def pangrams(s):
    # 알파벳은 총 26가지가 있다
    alphabet = [0] * 26
    
    for w in s :
        # 소문자를 기준으로 해당 알파벳이 사용된적이 있다면, 해당 알파벳 출현횟수를 1로 한다
        if 'a' <= w <= 'z' and alphabet[ord(w)-97] == 0 :
            alphabet[ord(w)-97] = 1
        # 대문자를 기준으로 해당 알파벳이 사용된적이 있다면, 해당 알파벳 출현횟수를 1로 한다
        elif 'A' <= w <= 'Z' and alphabet[ord(w)-65] == 0 :
            alphabet[ord(w)-65] = 1
    
    # 모든 알파벳이 한번씩 사용되었다면 pangram을 출력하고
    if sum(alphabet) == 26 :
        return "pangram"
    
    # 그렇지 않다면 not pangram을 출력한다
    else :
        return "not pangram"
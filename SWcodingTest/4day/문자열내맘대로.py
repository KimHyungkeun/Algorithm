def solution(strings, n):
    
    # 먼저 사전순으로 정렬 한 후, 인덱스 n을 기준으로 한번더 정렬한다
    strings.sort()
    strings.sort(key = lambda x : x[n])
    
    # answer = sorted(strings)
    print(strings)
    return strings

strings = ["abce", "abcd", "cdx"]
n = 2
solution(strings, n)
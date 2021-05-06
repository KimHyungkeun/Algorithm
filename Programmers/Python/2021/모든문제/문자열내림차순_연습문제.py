def solution(s):
    answer = ''

    # 해당 문자열을 리스트로 변환
    arr = list(s)
    # 문자열 각각 문자를 기준으로 내림차순 정렬
    arr.sort(reverse=True)
    # 정렬이 완료된 리스트를 다시 문자열로 환원
    answer = ''.join(arr)
    # 값 리턴
    return answer
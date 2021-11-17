class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 해당 문자열이 회문인지 검사
        # 들어오는 문자열 중, 오로지 알파벳과 숫자만을 가지고 판별하며, 알파벳은 대소문자를 가리지 않는다
        input_s = []
        s = s.lower()
        
        # 숫자나 알파벳만을 판별
        for w in s :
            if 'a' <= w <= 'z' or '0' <= w <= '9':
                input_s.append(w)
        
        # 들어오는 문자열 철자나 숫자에 대해, 역순으로 바꾼 내용도 저장
        reverse_input = list(reversed(input_s))
        print(input_s)
        print(reverse_input)
        
        # 두 문자열이 서로 같다면 회문이고 그렇지 않으면 회문이 아니다
        if input_s == reverse_input :
            return True
        else :
            return False
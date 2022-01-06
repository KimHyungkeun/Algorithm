# 두 문자열이 서로 같은 문자열인지 확인
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
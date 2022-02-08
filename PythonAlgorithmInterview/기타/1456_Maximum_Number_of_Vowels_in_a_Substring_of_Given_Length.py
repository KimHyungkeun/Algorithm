# 시간 초과
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        max_cnt = 0
        for i in range((len(s) - k) + 1) :
            sub_str  = s[i:i+k]
            
            cnt = 0
            for w in sub_str :
                if w in vowel :
                    cnt += 1
            # print(sub_str, cnt)
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt

# 정답 : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/discuss/659541/Python-sliding-window
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        max_cnt = 0
        
        cnt = 0
        for w in s[:k] :
            if w in vowel :
                cnt += 1
        max_cnt = cnt
        
        for i in range(len(s) - k) :
            if s[i] in vowel :
                cnt -= 1
            if s[i+k] in vowel :
                cnt += 1
            
            max_cnt = max(max_cnt, cnt)
            
        return max_cnt

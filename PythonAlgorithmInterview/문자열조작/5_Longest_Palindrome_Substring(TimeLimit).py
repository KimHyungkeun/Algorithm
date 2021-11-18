# 시간초과 풀이
# import time

# def isPalindrome(word) :
#     return word == word[::-1]

# s = "mozblnzrszxtdjmwvgeovtxoftpcsbnjryogrnibiiqfexljlfikfcxvrzrpfvugtdjrlkgvkmrqgeltifdehsewpdhpjpnuobmuozopmglnocqcozvratjpzrklexqdeuvvzfjkuknkkoynxptrgtzadmpfdkphfjhdulhzncoofmmrwqjxeyhodfavcgpjmohohuztezdxegqzbaaobzrqptuqsvwnfdneyccbkgkjafztytwuppvleukdqqzyeiltsvoqbxupbasiityganofxijucwzqgtdyxljociwwjdrnfnfbwyymmvbuvbrdnvcubzkohknbsneutrcukfiqqhfviqdsbtrldipenqifdcrenpuyaqvkparycksurhbtjppwhezbcgocamurdawimkzzkmiwadrumacogcbzehwppjtbhruskcyrapkvqayupnercdfiqnepidlrtbsdqivfhqqifkucrtuensbnkhokzbucvndrbvubvmmyywbfnfnrdjwwicojlxydtgqzwcujixfonagytiisabpuxbqovstlieyzqqdkuelvppuwtytzfajkgkbccyendfnwvsqutpqrzboaabzqgexdzetzuhohomjpgcvafdohyexjqwrmmfoocnzhludhjfhpkdfpmdaztgrtpxnyokknkukjfzvvuedqxelkrzpjtarvzocqconlgmpozoumbounpjphdpweshedfitlegqrmkvgklrjdtguvfprzrvxcfkifljlxefqiibinrgoyrjnbscptfoxtvoegvwmjdtxzsrznlbzom"
# longest_string = ""

# start = time.time()  # 시작 시간 저장
# for i in range(len(s)) :
#     for j in range(i, len(s)+1) :
#         origin = s[i:j]
        
#         if isPalindrome(origin) :
#             if len(origin) > len(longest_string) :
#                 longest_string = origin
    
# print(longest_string)    
# print("time :", time.time() - start)   

class Solution:
    
    
    def longestPalindrome(self, s: str) -> str:
            # 팰린드롬 판별 및 투 포인터 확장
            def expand(left, right) :
                while left >= 0 and right < len(s) and s[left] == s[right] :
                    left -= 1
                    right += 1
                return s[left+1:right]

            # 만약, 해당사항이 따로 없으면 바로 리턴
            if len(s) < 2 or s == s[::-1] :
                return s
            
            # 슬라이딩 윈도우 우측으로 이동
            result = ''
            for i in range(len(s) - 1) :
                result = max(result, expand(i, i+1), expand(i, i+2), key=len)
            
            return result
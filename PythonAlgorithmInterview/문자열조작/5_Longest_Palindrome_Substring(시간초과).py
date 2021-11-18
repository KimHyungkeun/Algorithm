import time


def isPalindrome(word) :
    return word == word[::-1]

s = "mozblnzrszxtdjmwvgeovtxoftpcsbnjryogrnibiiqfexljlfikfcxvrzrpfvugtdjrlkgvkmrqgeltifdehsewpdhpjpnuobmuozopmglnocqcozvratjpzrklexqdeuvvzfjkuknkkoynxptrgtzadmpfdkphfjhdulhzncoofmmrwqjxeyhodfavcgpjmohohuztezdxegqzbaaobzrqptuqsvwnfdneyccbkgkjafztytwuppvleukdqqzyeiltsvoqbxupbasiityganofxijucwzqgtdyxljociwwjdrnfnfbwyymmvbuvbrdnvcubzkohknbsneutrcukfiqqhfviqdsbtrldipenqifdcrenpuyaqvkparycksurhbtjppwhezbcgocamurdawimkzzkmiwadrumacogcbzehwppjtbhruskcyrapkvqayupnercdfiqnepidlrtbsdqivfhqqifkucrtuensbnkhokzbucvndrbvubvmmyywbfnfnrdjwwicojlxydtgqzwcujixfonagytiisabpuxbqovstlieyzqqdkuelvppuwtytzfajkgkbccyendfnwvsqutpqrzboaabzqgexdzetzuhohomjpgcvafdohyexjqwrmmfoocnzhludhjfhpkdfpmdaztgrtpxnyokknkukjfzvvuedqxelkrzpjtarvzocqconlgmpozoumbounpjphdpweshedfitlegqrmkvgklrjdtguvfprzrvxcfkifljlxefqiibinrgoyrjnbscptfoxtvoegvwmjdtxzsrznlbzom"
longest_string = ""

start = time.time()  # 시작 시간 저장
for i in range(len(s)) :
    for j in range(i, len(s)+1) :
        origin = s[i:j]
        
        if isPalindrome(origin) :
            if len(origin) > len(longest_string) :
                longest_string = origin
    
print(longest_string)    
print("time :", time.time() - start)   
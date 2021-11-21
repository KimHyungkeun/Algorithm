class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels에 담긴 각 보석의 갯수를 stones에서 찾아낸다
        jewel_dict = {}
        for j in jewels :
            jewel_dict[j] = 0
        
        for s in stones :
            if s not in jewel_dict :
                continue
            jewel_dict[s] += 1
        
        return sum(jewel_dict.values())
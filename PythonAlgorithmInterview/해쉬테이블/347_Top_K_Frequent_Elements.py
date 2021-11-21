class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums에 등장하는 숫자 빈도수 중, 상위 k개까지 리스트에 담아 리턴한다
        result = []
        set_nums = list(set(nums))
        
        nums_dict = {}
        # nums에 등장하는 숫자들의 종류
        for s in set_nums :
            nums_dict[s] = 0
        
        # 각 숫자별로 등장빈도수 추가
        for n in nums :
            nums_dict[n] += 1
        
        # 등장 빈도수 별로 내림차순 정렬(가장 많이 등장하는 상위 갯수부터 세므로)
        sorted_nums = sorted(nums_dict.items(), reverse=True, key = lambda item : item[1])
        print(sorted_nums)

        # 상위 k개까지 result 리스트에 담을 수 있도록한다 
        for s in sorted_nums :
            result.append(s[0])
            if len(result) == k :
                break
        
        return result
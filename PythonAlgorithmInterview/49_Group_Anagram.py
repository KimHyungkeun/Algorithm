class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 아나그램 단어를 그룹화 시키기 위한 딕셔너리
        anagram_dict = {}
        result = []
        
        # 단어들 각각을 오름차순 정렬하여 통일성을 유지
        # 그 후, 정렬된 단어들에 대해서 비교하여 서로 같은 종류의 아나그램인지 확인 후에 그룹화 시킨다
        for s in strs :
            key = ''.join(sorted(list(s)))
            if key in anagram_dict :
                anagram_dict[key].append(s)
            else :
                anagram_dict[key] = [s]
        
        # 그룹화 시킨 딕셔너리 내에서, 단어별로 한번더 오름차순 한다
        for key in anagram_dict.keys() :
            anagram_dict[key].sort()
            result.append(anagram_dict[key])
        
        return result
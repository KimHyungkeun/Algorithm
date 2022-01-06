class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 주어진 구간이 한곳 밖에 없다면 그대로 반환
        if len(intervals) == 1 :
            return intervals
        
        ans = []
        intervals.sort(key = lambda x : x[0])
        
        # 구간별 상세 요소파악을 위해 start~end까지의 수를 모두 구함
        arr = []
        for inter in intervals :
            arr.append([i for i in range(inter[0], inter[1]+1)])
        

        # 서로 겹치는 구간을 찾는다. (교집합을 통해 맞물리는 구간을 구한 후, 한개이상이라도 있다면 합집합을 통해 두 구간을 병합)
        ans.append(arr[0])
        for i in range(1, len(arr)) :
            if len(set(ans[-1]) & set(arr[i])) >= 1 :
                ans[-1] = list(set(ans[-1]) | set(arr[i]))
                
            else :
                ans.append(arr[i])
            
        
        # 병합된 구간을 출력
        result = []
        for a in ans :
            result.append([min(a), max(a)])
        return result
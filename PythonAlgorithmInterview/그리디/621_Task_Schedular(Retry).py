import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        # print(counter)
        
        while True :
            sub_cnt = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1) :
                sub_cnt += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
            
            if not counter :
                break
            
            result += (n - sub_cnt + 1)
        
        return result
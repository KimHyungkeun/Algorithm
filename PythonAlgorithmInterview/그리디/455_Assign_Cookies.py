class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # 나눠줄 쿠키가 없으면 0개 리턴
        if not s :
            return 0
        
        # 스택을 통한 pop 진행을 위해, 내림차순 정렬
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        # 해당 쿠키가 나눠줄 수 있는 쿠키면 cnt를 증가
        cnt = 0
        while g and s :
            if g[-1] <= s[-1] :
                s.pop()
                g.pop()
                cnt += 1
            else :
                s.pop()
            
        
        return cnt
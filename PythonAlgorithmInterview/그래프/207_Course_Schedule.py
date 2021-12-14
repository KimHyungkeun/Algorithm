# 실패코드(타임아웃)
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites :
            graph[x].append(y)
        
        traced = set()
        
        def dfs(i) :
            # 순환 구조이면 False
            if i in traced :
                return False
            
            traced.add(i)
            for y in graph[i] :
                if not dfs(y) :
                    return False
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph) :
            if not dfs(x) :
                return False
        
        return True

# 정답코드
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites :
            graph[x].append(y)
        
        traced = set()
        visited = set()

        def dfs(i) :
            # 순환 구조이면 False
            if i in traced :
                return False
            
            # 이미 방문한 노드이면 True
            if i in visited :
                return True

            traced.add(i)
            for y in graph[i] :
                if not dfs(y) :
                    return False
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드에 등록
            visited.add(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph) :
            if not dfs(x) :
                return False
        
        return True

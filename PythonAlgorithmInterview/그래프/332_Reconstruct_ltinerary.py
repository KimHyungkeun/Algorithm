# 실패 코드
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        graph = {}
        for t in tickets :
            if t[0] not in graph :
                graph[t[0]] = [t[1]]
            else :
                graph[t[0]].append(t[1])
            
            if t[1] not in graph :
                graph[t[1]] = []

        
        for key in graph.keys() :
            graph[key].sort()
            
      
        def dfs(graph, start) :
            
            result.append(start)
            
            if not graph[start] :
                return
            
            for g in graph[start] :
                if graph[start] :
                    graph[start].pop(0)
                dfs(graph, g) 
                
        
        dfs(graph, "JFK")
        return result

# 정답 코드
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        graph = {}
        for t in tickets :
            if t[0] not in graph :
                graph[t[0]] = [t[1]]
            else :
                graph[t[0]].append(t[1])
            
            if t[1] not in graph :
                graph[t[1]] = []

        
        for key in graph.keys() :
            graph[key].sort()
            
       
        def dfs(start) :
            while graph[start] :
                dfs(graph[start].pop(0))
            result.append(start)
                
        
        dfs("JFK")
        return result[::-1]
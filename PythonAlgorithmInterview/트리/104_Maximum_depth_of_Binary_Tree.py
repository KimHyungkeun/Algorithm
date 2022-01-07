class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
     
        q = deque([root])
        depth = 0
        
        while q :
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(q)) :
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
        
        # BFS 반복 횟수 == 깊이
        return depth

# DFS 풀이
class Solution:
    max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return 0
        
        depth = 0
        def dfs(node, depth) :
            
            if node is None :
                self.max_depth = max(self.max_depth, depth)
                return
                        
            dfs(node.left, depth+1)      
            dfs(node.right, depth+1)
                

        dfs(root, depth)  
        return self.max_depth

# DFS 풀이2
class Solution:
    max_depth = 0
    
    def dfs(self, node, depth) :                 
        if node is None :
            self.max_depth = max(self.max_depth, depth)
            return
        self.dfs(node.left, depth+1)                  
        self.dfs(node.right, depth+1)
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        if root is None :
            return 0
        
        depth = 0
        self.dfs(root, depth)  
        return self.max_depth
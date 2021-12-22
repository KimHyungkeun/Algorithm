# DFS 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        stack = deque([root])
        while stack :
            node = stack.pop()
            # 부모 노드로부터 하향식 스왑
            if node :
                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)

        return root

# BFS 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        q = deque([root])
        while q :
            node = q.popleft()
            # 부모 노드로부터 하향식 스왑
            if node :
                node.left, node.right = node.right, node.left
                
                q.append(node.left)
                q.append(node.right)

        return root
        
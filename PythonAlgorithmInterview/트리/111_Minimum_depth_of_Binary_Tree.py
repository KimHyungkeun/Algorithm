from collections import deque
class Solution:   
    def minDepth(self, T: Optional[TreeNode]) -> int:

        if T is None :
            return 0
        
        queue = deque([T])
        depth = 0
        
        while queue :
            
            depth += 1
            
            for _ in range(len(queue)) :
                cur_node = queue.popleft()
                left_flag = False
                right_flag = False
                
                if cur_node.left :
                    queue.append(cur_node.left)
                    left_flag = True
                if cur_node.right :
                    queue.append(cur_node.right)
                    right_flag = True
                
                if not left_flag and not right_flag :
                    return depth
        
        return depth
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    total : int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # low 이상 high 이하의 노드값들의 합을 구한다
        if root :
            self.rangeSumBST(root.left,low,high)
            if low <= root.val <= high :
                self.total += root.val
            self.rangeSumBST(root.right,low,high)
        
        return self.total
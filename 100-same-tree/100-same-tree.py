# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val != q.val:
            return False
        
        
        stack = []
        stack.append((p, q))
        
        while stack != []:
            t1, t2 = stack.pop()
            
            if (t1 and not t2) or (not t1 and t2):
                return False
            
            if t1 and t2:
                if t1.val != t2.val:
                    return False
                stack.append((t1.right, t2.right))
                stack.append((t1.left, t2.left))
        
        return True
            
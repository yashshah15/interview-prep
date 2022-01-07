# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        
        stack = []
        stack.append((root1, root2))
        
        while stack:
            t = stack.pop()
            if t[0] == None or t[1] == None:
                continue
            
            t[0].val += t[1].val
            
            #if tree1 has null in the left sub child
            if not t[0].left:
                t[0].left = t[1].left
            
            else:
                stack.append((t[0].left, t[1].left))
            
            #if tree1 has null in the right sub child
            if not t[0].right:
                t[0].right = t[1].right
            
            else:
                stack.append((t[0].right, t[1].right))
        
        return root1
                
            
                        
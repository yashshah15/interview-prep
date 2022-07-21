from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        level = 0
        levels = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            levels.append([])
            for i in range(level_size):
                current  = queue.popleft()
                levels[level].append(current.val)
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
            
            level += 1
        
        return levels
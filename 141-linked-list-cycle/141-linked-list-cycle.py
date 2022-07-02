from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
visited = defaultdict(int)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ptr = head
        if not head:
            return False
        if ptr.next == None:
            return False
        
        while ptr:
            if visited[ptr] == 0:
                visited[ptr] = 1
            
            else:
                return True
            
            ptr = ptr.next
        
        return False
            
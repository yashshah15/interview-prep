# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            temp = ptr.next
            last = stack.pop()
            
            ptr.next = last
            last.next = temp
            
            ptr = temp
            
            if ptr and ptr.next == last:
                ptr.next = None
                break
            
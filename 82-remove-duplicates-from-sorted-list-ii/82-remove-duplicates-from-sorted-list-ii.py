# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 1st, process the head-duplicate
        while head.next != None and head.val == head.next.val:
            h = head.next
            while h != None and h.val == head.val:
                h = h.next
            if h is None:
                # all elements in the linked list are same-valued
                return h
            # reset head after this head-duplicate segment
            head = h

        if head.next is None:
            # for example: [1, 1, 1, 2], then return [2]
            return head

        # 2nd, use multiple pointers to remove each following duplicate segments
        p1, p2 = head.next, head
        while True:
            # locate the starting node of the next duplicate segment by p1 pointer
            while p1.next != None and p1.val != p1.next.val:
                p1 = p1.next
                p2 = p2.next

            if p1.next is None:
                # this means there are no more duplicates, so we have finished our task
                return head
            else:
                # locate the ending node of this duplicate segment by p1 pointer
                while p1.next != None and p1.val == p1.next.val:
                    p1 = p1.next

                # remove this duplicate segment by setting "p2.next = p1.next", and move the p1 pointer
                # to the next node if it exists to continue scanning the next duplicate segment
                p2.next = p1.next
                if p1.next != None:
                    p1 = p1.next
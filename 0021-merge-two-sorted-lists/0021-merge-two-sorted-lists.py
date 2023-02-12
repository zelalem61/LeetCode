# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        n = dummy
        n1 = list1
        n2 = list2
        while n1 and n2:
            if n2.val > n1.val:
                n.next = n1
                n1 = n1.next
            else: 
                n.next = n2
                n2 = n2.next
            n = n.next
        if n1: n.next = n1
        elif n2: n.next = n2
        return dummy.next
        
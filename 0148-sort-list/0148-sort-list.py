# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        
        cur = head
        while cur:
            sorted_list.append(cur.val)
            cur = cur.next
        sorted_list.sort()
        
        dummy = ListNode()
        current = dummy
        for val in sorted_list:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
        
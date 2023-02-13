# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        last = dummyHead
        while last and last.next:
            if last.next and last.next.next and last.next.val == last.next.next.val:
                self.removeDuplicate(last)
            else:
                last = last.next
        return dummyHead.next
    def removeDuplicate(self, last):
        start = last.next
        end = last.next.next
        
        while end.next:
            if end.next.val == start.val:
                end = end.next
            else:
                break
        last.next = end.next
        
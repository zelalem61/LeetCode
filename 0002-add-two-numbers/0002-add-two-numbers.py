# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = ""
        right = ""
        current1 = l1
        current2 = l2
        while current1:
            left += str(current1.val)
            current1 = current1.next
        while current2:
            right += str(current2.val)
            current2 = current2.next
        left = int(left[::-1])
        right = int(right[::-1])
        sumOfTwo = left + right
        sumOfTwo = str(sumOfTwo)[::-1]
        
        result = ListNode()
        curr = result
        for i in sumOfTwo:
            node = ListNode(int(i))
            curr.next = node
            curr = curr.next
        return result.next

        
        
        
        
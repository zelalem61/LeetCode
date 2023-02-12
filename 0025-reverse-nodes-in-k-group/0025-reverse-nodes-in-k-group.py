# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        finalNodes = []
        while head:
            stack = []
            for _ in range(k):
                if head:
                    stack.append(head)
                    head = head.next
                else:
                    break
            if len(stack) == k:
                finalNodes+=stack[::-1]
            else:
                finalNodes+=stack
        for i in range(len(finalNodes)):
            if i < len(finalNodes)-1:
                finalNodes[i].next = finalNodes[i+1]
            else:
                finalNodes[i].next = None
        return finalNodes[0]
        
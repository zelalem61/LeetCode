# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        n = len(arr)
        if n == 0:
            return head
        k = k % n  

        for _ in range(k):
            temp = arr[-1]  
            for i in range(n - 1, 0, -1):
                arr[i] = arr[i - 1]  
            arr[0] = temp 

        if not arr:
            return None

        rotated_head = ListNode(arr[0])
        current = rotated_head
        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            current.next = new_node
            current = current.next

        return rotated_head
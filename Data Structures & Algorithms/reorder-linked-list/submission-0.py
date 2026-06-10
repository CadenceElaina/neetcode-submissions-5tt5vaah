# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at the middle. Split the list into two havles.
        second = slow.next
        slow.next = None # Disconnect the first half from the second half

        # Step 2: Reverse the second half of the list
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 'prev' is now the head of the reversed second half
        first, second = head, prev

        # Step 3: Merge the two sorted ~ halves alternatingly
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        # two halves we want to zip together
        # [1,2,3,4,5,6]
        # find the middle: [1,2,3] and [4,5,6]
        # reverse the second half [4,5,6] and [6,5,4]
        # 1 -> 6 -> 2 -> 5 -> 3 ->4                    

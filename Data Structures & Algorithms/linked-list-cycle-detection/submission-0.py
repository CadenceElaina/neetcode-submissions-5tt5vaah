# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if index = -1 --- tail node -> null
        # index = 1 from 1,2,3,4 then 4 -> 2
        # how do i access the index value? its not input into the fn so i mean head.index?

        curr = head
        seen=set()
        i = 0

        while curr:
            seen.add(curr)
            temp = curr.next
            if temp in seen:
                return True
            #if curr.val in seen.values():
             #   if curr.next == None or -1:
              #      return False
            #seen[curr.val] = seen.get(curr.val, i) 
            curr=curr.next
            #seen[i] = curr.val
              #  if curr.next == None:
               #     return False
            
                #if curr.next in seen:
                   # return True
               # 


        # if we exit while that means tail points to None and return False
        return False
            # store prev vals in HM if we encounter a value after pointing to prior value in
            # our hashmap then we know its the tai and return True
            # repeating values?

         #   seen[curr.val] = seen.get(curr.val,0)+1

            
            #if curr == curr.index:
             #   nodeIndex = curr
            #if curr.next = None:
             #   curr.next = nodeIndex
              #  break
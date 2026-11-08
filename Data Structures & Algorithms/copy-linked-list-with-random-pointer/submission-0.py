"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None} # : not , why it needs to be filled with none - if we reach a node thats next is empty
        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy # The hashmaps key is the node were on so that in the next loop we can use the cur node to get the copied version to store in the new LL? 
            cur = cur.next # cant just call cur.next you have to update the actual node to be the next one. 
        
        cur = head # forgot you could just reassign it tbh

        while cur:
            # update hm to store val, next, and rand
            copy = oldToCopy[cur] # find the current node within the HM and store it to a new node
            copy.next = oldToCopy[cur.next] # get the next val from the hm and store it in our copy
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head] # returns the head of the new deep copied LL
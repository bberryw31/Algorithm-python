from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for l in lists:
            if l:  # check if the ListNode is not None
                print(l.val)
            else:
                print(None)

# Example usage:
# Create the linked lists manually
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node2.next = node3

lists = [node1, None, None, node2]

# Instantiate the Solution class
solution = Solution()
solution.mergeKLists(lists)

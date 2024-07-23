from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        it = result
        ad = 0
        while l1 and l2:
            s = l1.val + l2.val + ad
            ad = 0
            if s > 9:
                s -= 10
                ad = 1
            it.next = ListNode(s)
            it = it.next
            l1 = l1.next
            l2 = l2.next
        while ad and l1:
            s = l1.val + ad
            ad = 0
            if s > 9:
                s -= 10
                ad = 1
            l1 = l1.next
            it.next = ListNode(s)
            it = it.next
        while ad and l2:
            s = l2.val + ad
            ad = 0
            if s > 9:
                s -= 10
                ad = 1
            l2 = l2.next
            it.next = ListNode(s)
            it = it.next
        if l1:
            it.next = l1
        elif l2:
            it.next = l2
        elif ad:
            it.next = ListNode(1)
        return result.next
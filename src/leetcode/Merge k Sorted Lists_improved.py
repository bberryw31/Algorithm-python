from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        it = result
        k = len(lists)
        change = True
        while change == True:
            change = False
            minv = 10**4
            for l in lists:
                if l != None and l.val<minv:
                    minv = l.val
            for i in range(k):
                while lists[i] != None and lists[i].val == minv:
                    it.next = lists[i]
                    it = it.next
                    lists[i] = lists[i].next
                    change = True
        return result.next
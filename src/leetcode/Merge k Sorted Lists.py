from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        tempresult = result
        k = len(lists)
        change = True
        while change == True:
            change = False
            minv = [10**4,0]
            for i in range(k):
                if lists[i] != None and lists[i].val < minv[0]:
                    minv[0] = lists[i].val
                    minv[1] = i
                    change = True
            if change == True:
                tempresult.next = lists[minv[1]]
                lists[minv[1]] = lists[minv[1]].next
                tempresult = tempresult.next
        return result.next
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self,list1,list2):
        result = ListNode()
        it = result
        while list1 and list2:
            if list1.val < list2.val:
                it.next = list1
                list1 = list1.next
            else:
                it.next = list2
                list2 = list2.next
            it = it.next

        if list1:
            it.next = list1
        if list2:
            it.next = list2
        return result.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None

        if k == 1:
            return lists[0]

        pre = self.mergeKLists(lists[:k//2])
        post = self.mergeKLists(lists[k//2:])

        return self.merge(pre,post)
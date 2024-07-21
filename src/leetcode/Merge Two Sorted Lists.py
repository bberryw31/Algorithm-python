from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result2 = result
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                result2.next = list1
                list1 = list1.next
            else:
                result2.next = list2
                list2 = list2.next
            result2= result2.next
        if list1 == None:
            result2.next = list2
        else:
            result2.next = list1
        return result.next


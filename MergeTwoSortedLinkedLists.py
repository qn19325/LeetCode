# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = headToReturn = ListNode()
    while list1 and list2:               
        if list1.val < list2.val:
            cur.next = list1
            cur = list1
            list1 = list1.next
        else:
            cur.next = list2
            cur = list2
            list2 = list2.next
            
    if list1 or list2: # when the are elements left in only one of the lists
        cur.next = list1 if list1 else list2
        
    return headToReturn.next
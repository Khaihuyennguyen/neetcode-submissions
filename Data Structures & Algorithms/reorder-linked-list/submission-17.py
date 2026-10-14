# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        
        list1 = head
        list2 = prev
   

        while list2:
            temp1 = list1.next
            list1.next = list2
            temp2 = list2.next
            list2.next = temp1
            list1 = temp1
            list2 = temp2
        
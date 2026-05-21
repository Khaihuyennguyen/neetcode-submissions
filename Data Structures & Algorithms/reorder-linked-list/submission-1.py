# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        head2 = slow.next
        slow.next = None
        nextNode = None
        prev = None
        while head2:
            nextNode = head2.next
            head2.next = prev
            prev = head2
            head2 = nextNode
        
        head1, head2 = head, prev

        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        
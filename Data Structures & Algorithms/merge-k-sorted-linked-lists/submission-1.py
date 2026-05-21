# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwoLinklist(list1, list2):
            newHead = ListNode()
            dummyNode = newHead
            while list1 and list2:
                if list1.val > list2.val:
                    dummyNode.next = list2
                    list2 = list2.next
                else:
                    dummyNode.next = list1
                    list1 = list1.next
                dummyNode = dummyNode.next
            
            if list1:
                dummyNode.next = list1
            if list2:
                dummyNode.next = list2
            return newHead.next

        
        index = 0

        while len(lists) > 1:
            newList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                newList.append(mergeTwoLinklist(l1, l2))
            lists = newList
        return lists[0]



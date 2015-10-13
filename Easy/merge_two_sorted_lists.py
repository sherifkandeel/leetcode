# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        merged = None
        start = None
        while l1 != None:
            if l2 == None or l1.val <= l2.val:
                if merged == None:
                    merged = ListNode(l1.val)
                    start = merged
                else:
                    merged.next = ListNode(l1.val)
                    merged = merged.next
                l1 = l1.next
            elif l2.val < l1.val:
                if merged == None:
                    merged = ListNode(l2.val)
                    start = merged
                else:
                    merged.next = ListNode(l2.val)
                    merged = merged.next
                l2 = l2.next
        
        while l2 != None:
            merged.next = ListNode(l2.val)
            merged = merged.next
            l2 = l2.next
            
        return start
                
                
        
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        

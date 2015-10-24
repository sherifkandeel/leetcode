# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        temp = head.next
        head.next = head.next.next
        temp.next = head
        head = temp
        prev = head.next
        if not prev.next or not prev.next.next: 
            return head
        
        first = prev.next
        second = prev.next.next
        while first and second:
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            if not first.next: break
            first = first.next
            second = first.next
        return head
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

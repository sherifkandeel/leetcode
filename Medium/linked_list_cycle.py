# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        slow = head
        fast = head
        if fast.next!=None and fast.next.next != None:
            fast = fast.next.next
        while fast.next !=None and fast.next.next != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return None
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return None
        start = head
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return start
            
        # Another solution: 
        #
        # if head == None:
        #     return None
        # prev = None
        # start = head
        # while head != None:
        #     if head.val == val:
        #         if prev == None:
        #             head = head.next
        #             start = head
        #             continue
        #         else:
        #             prev.next = head.next
        #     else:
        #         if prev != None:
        #             prev = prev.next
        #         else:
        #             prev = head
        #     head = head.next
        # return start
        
        
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        

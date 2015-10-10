# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        start = head
        lastpart = head
        cutoff = n+1
        cnt = 1
        while start != None:
            if cutoff<cnt:
                lastpart = lastpart.next
            start = start.next
            cnt += 1
        if cnt -1 == n:
            head = head.next
        if lastpart.next != None:
            lastpart.next = lastpart.next.next
        return head
            
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        

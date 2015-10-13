#Some memory shit because python!
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def navigate(self, head, start):
        if head == None:
            return True
        return self.navigate(head.next, start)
        isequal = (head.val != start.val)
        start = start.next
        return isequal
            
                
    def isPalindrome(self, head):
        return self.navigate(head, head)
        
        """
        :type head: ListNode
        :rtype: bool
        """
        

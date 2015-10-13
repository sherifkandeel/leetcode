# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def getLength (self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length
        
    def getIntersectionNode(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        while lenB > lenA:
            headB = headB.next
            lenB-=1
        while lenA > lenB:
            headA = headA.next
            lenA -=1
        while headA != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
        
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        

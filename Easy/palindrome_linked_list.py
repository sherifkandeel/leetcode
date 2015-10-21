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
        

##'
#Now this solution works
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        #now fast is at the end and slow is at the middle
        #Now we reverse the middle to last linked list
        secondhead = slow.next
        p1 = secondhead
        p2 = p1.next
        # while p1 != None and p2 != None:
        while p2!= None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        secondhead.next = None
        if p1 == None:
            secondhead = p2
        else:
            secondhead = p1
        while secondhead != None:
            if secondhead.val != head.val:
                return False
            secondhead = secondhead.next
            head = head.next
        return True
        
            
       
        """
        :type head: ListNode
        :rtype: bool
        """
        

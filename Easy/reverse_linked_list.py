# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        s = Stack()
        while head != None:
            s.push(head.val)
            head = head.next
        start = ListNode(s.pop())
        new_head = start
        while not s.isEmpty():
            start.next = ListNode(s.pop())
            start = start.next
        return new_head
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

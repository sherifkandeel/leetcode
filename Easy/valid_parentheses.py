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
    def isValid(self, s):
        stack = Stack()
        for c in s:
            if c == '}' or c == ')' or c == ']':
                if stack.isEmpty():
                    return False
                cc = stack.pop()
                if (c == '}' and cc != '{') or (c == ']' and cc != '[') or (c == ')' and cc != '('):
                    return False
            else:
                stack.push(c)
        if not stack.isEmpty():
            return False
        return True
                    
                    
                
                
        """
        :type s: str
        :rtype: bool
        """
        

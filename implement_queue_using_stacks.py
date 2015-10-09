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


class Queue(object):
    def __init__(self):
        self.stack = Stack()
        

    def push(self, x):
        temp = Stack()
        while not self.stack.isEmpty():
            temp.push(self.stack.pop())
        self.stack.push(x)
        while not temp.isEmpty():
            self.stack.push(temp.pop())
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        return self.stack.pop()
        

    def peek(self):
        return self.stack.peek()
        """
        :rtype: int
        """
        

    def empty(self):
        return self.stack.isEmpty()
        """
        :rtype: bool
        """
        

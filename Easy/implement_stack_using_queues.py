from Queue import *
class Stack(object):
    def __init__(self):
        self.q = Queue()
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        temp = Queue()
        while not self.q.empty():
            temp.put(self.q.get())
        self.q.put(x)
        while not temp.empty():
            self.q.put(temp.get())
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        if not self.q.empty():
            self.q.get()
        """
        :rtype: nothing
        """
        

    def top(self):
        if not self.q.empty():
            t = self.q.get()
            self.push(t)
            return t
        
        """
        :rtype: int
        """
        

    def empty(self):
        return self.q.empty()
        """
        :rtype: bool
        """
        

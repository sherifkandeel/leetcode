class MinStack(object):
    def __init__(self):
        self.items = []
        self.minimum = 0

    def push(self, x):
        if self.items == []:
            self.minimum = x
        elif x < self.minimum:
            self.minimum = x
        self.items.append(x)
        

    def pop(self):
        item = self.items.pop()
        if item == self.minimum:
            if self.items != []:
                self.minimum = sorted(self.items)[0]
            else:
                self.minimum = 0
        return item
        

    def top(self):
        return self.items[len(self.items)-1]
        

    def getMin(self):
        return self.minimum
        """
        :rtype: int
        """
        

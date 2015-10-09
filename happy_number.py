class Solution(object):
    def squares_sum(self, n):
        sqs = 0
        while n > 0:
            sqs += (n%10)**2
            n /= 10
        return sqs
            
    def isHappy(self, n):
        s = set()
        sqs = n
        while sqs > 1:
            sqs = self.squares_sum(sqs)
            if sqs in s:
                return False
            else:
                s.add(sqs)
        return True
            
        
        """
        :type n: int
        :rtype: bool
        """
        

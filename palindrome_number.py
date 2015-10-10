class Solution(object):
    def get_length(self, x):
        count = 0
        while x> 0:
            x/=10
            count +=1
        return count
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        
        length = self.get_length(x)
        for i in range(length/2):
            right = x%10
            left = (x - (x%10**(length-1))) /10**(length-1)
            # print right, left
            if right != left:
                return False
            x = (x%10**(length-1))/10
            length -= 2
        return True
            
            
        """
        :type x: int
        :rtype: bool
        """
        

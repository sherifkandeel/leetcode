class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num

        summation = 0
        while num > 0:
            summation += num%10
            num /= 10
        return self.addDigits(summation)
        
                                                

solution = Solution()
print solution.addDigits(38)
                                                        

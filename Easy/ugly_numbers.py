class Solution(object):
    def get_prime_factors(self, num):
        factors = []
        if num % 2 == 0:
            factors.append(2)
        while num % 2 == 0:
            num = num/2
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                factors.append(i)
            while num % i == 0:
                num /= i
        if num > 2:
            factors.append(num)
        return factors
        
    def isUgly(self, num):
        if num <=0:
            return False
        if num <=6:
            return True
        factors = self.get_prime_factors(num)
        for f in factors:
            if f != 2 and f!= 3 and f!=5:
                return False
        return True
                
                
        
                    
        """
        :type num: int
        :rtype: bool
        """
       

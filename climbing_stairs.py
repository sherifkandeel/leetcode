#it's basically a fibonacci sequence
#number of distinct ways to climb n stairs is Fib(n)

d = {}
d[1] = 1
d[2] = 2
class Solution(object):
    def climbStairs(self, n):
        global d
        if n == 1 or n == 2: 
            return n
        if n in d:
            return d[n] 
        else:
            num1 = self.climbStairs(n-1)
            num2 = self.climbStairs(n-2)
            d[n] = num1+num2
            return num1+num2
        
        
      

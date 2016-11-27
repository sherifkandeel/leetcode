import math

class Solution(object):
    def __init__(self):
        self.factorials = {}

    def factorial(self, n):
        if n <= 1:
            return 1
        return n*self.factorial(n-1)
    
    def getFactorial(self, n):
        if n not in self.factorials:
            self.factorials[n] = self.factorial(n)
        return self.factorials[n]

    def calculateDistance(self, p1, p2):
        return math.sqrt(((p1[0] - p2[0])*(p1[0] - p2[0])) + ((p1[1] - p2[1])*(p1[1] - p2[1])))

    def countBoomerangs(self, hs):
        counter = 0
        for k,v in hs.items():
            if v > 1:
                counter += (self.getFactorial(v)/(self.getFactorial(v-2)))
        return counter


    def numberOfBoomerangs(self, points):
        counter = 0
        for i in range(len(points)):
            temphash = {}
            for j in range(len(points)):
                if i == j: continue
                distance = self.calculateDistance(points[i], points[j])
                if distance in temphash:
                    temphash[distance] += 1
                else:
                    temphash[distance] = 1
            counter += self.countBoomerangs(temphash)
        return counter

        
# s = Solution()
# example = [[0,0],[1,0],[-1,0],[0,1],[0, -1]]
# print(s.numberOfBoomerangs(example))

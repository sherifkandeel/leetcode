from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secc = Counter(secret)
        for i in guess:
            if i in secc and secc[i]>0:
                cows+=1
                secc[i]-=1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                cows -= 1
            
        return str(bulls)+"A"+str(cows)+"B"
                    
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        

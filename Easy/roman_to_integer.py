class Solution(object):
    def romanToInt(self, s):
        romand = {}
        romand['I'] = 1
        romand['V'] = 5
        romand['X'] = 10
        romand['L'] = 50
        romand['C'] = 100
        romand['D'] = 500
        romand['M'] = 1000
        
        
        sl = list(s)
        sl.reverse()
        result = 0
        for i in range(len(sl)):
            if i == 0:
                result += romand[sl[i]]
                continue
            if romand[sl[i]] < romand[sl[i-1]]:
                result -= romand[sl[i]]
            else:
                result+= romand[sl[i]]
        return result
            
            
        
        """
        :type s: str
        :rtype: int
        """
        

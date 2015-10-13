class Solution(object):
    def hammingWeight(self, n):
        n_str = str(bin(n)[2:])
        weight = 0
        for c in n_str:
            if c == '1':
                weight +=1
        return weight
        
        

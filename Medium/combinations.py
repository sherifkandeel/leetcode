import copy
class Solution(object):
    def generate(self, ls, cur, num, n, k):
        if num > 0:
            cur.append(num)
        if len(cur) == k:
            ls.append(cur)
            return
        for i in range(num+1, n+1):
            self.generate(ls, copy.deepcopy(cur), i, n, k)
            
            
    def combine(self, n, k):
        ls = []
        self.generate(ls, [], 0, n, k)
        return ls
        
                
        
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        

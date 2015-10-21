class Solution(object):
    def draw(self, res, n, opened, closed, sofar):
        if closed > opened:
            return
        if opened == n and closed == n:
            res.append(sofar)
        if opened <=n:
            self.draw(res, n, opened+1, closed, sofar+"(")
        if closed <=n:
            self.draw(res, n, opened, closed+1, sofar+")")
        
        
    def generateParenthesis(self, n):
        res = []
        self.draw(res, n, 0, 0, "")
        return res
        """
        :type n: int
        :rtype: List[str]
        """
         

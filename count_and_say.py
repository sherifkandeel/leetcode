class Solution(object):
    def countnum(self, n):
        cnt = 0
        counted = []
        for i in range(len(n)):
            if i == 0:
                cnt= 1
                continue
            if n[i] != n[i-1]:
                counted.append(cnt)
                counted.append(n[i-1])
                cnt = 0
            cnt +=1
        counted.append(cnt)
        counted.append(n[len(n)-1])
        return counted
    def countAndSay(self, n):
        nn = [1]
        for i in range(n-1):
            nn = self.countnum(nn)
        return ''.join(map(str, nn))
            
        """
        :type n: int
        :rtype: str
        """
        

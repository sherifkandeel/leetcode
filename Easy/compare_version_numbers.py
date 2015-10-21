class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range((min(len(v1),len(v2)))):
            if int(v1[i])>int(v2[i]):
                return 1
            if int(v1[i])<int(v2[i]):
                return -1
        if len(v1) > len(v2) and int(v1[-1])>0:
            return 1
        if len(v1) < len(v2) and int(v2[-1])>0:
            return -1
        return 0
        
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        


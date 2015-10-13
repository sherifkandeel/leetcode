class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for i in range(len(t)):
            if s[i] in sd:
                sd[s[i]] += 1
            else:
                sd[s[i]] = 1
            
            if t[i] in td:
                td[t[i]] += 1
            else:
                td[t[i]] = 1
        
        for k, v in sd.items():
            if k not in td:
                return False
            if td[k] != sd[k]:
                return False
        return True
        
        

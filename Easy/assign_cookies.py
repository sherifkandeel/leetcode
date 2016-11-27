class Solution(object):
    def findContentChildren(self, g, s):
        children = sorted(g)
        cookies = sorted(s)
        content = 0
        childPointer = 0
        cookiePointer = 0
        while cookiePointer < len(cookies) and childPointer < len(children):
            if children[childPointer] <= cookies[cookiePointer]:
                content += 1
                childPointer += 1
            cookiePointer += 1
        return content


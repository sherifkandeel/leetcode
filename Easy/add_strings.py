class Solution(object):
    def addStrings(self, num1, num2):
        ordOffset = 48
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        maxlen = max(len(num1), len(num2))
        res = ""
        # for i in range(maxlen - 1, -1, -1):
        for i in range(maxlen):

            n1 = (ord(num1[i]) - ordOffset) if i < len(num1) and i >= 0 else 0
            n2 = (ord(num2[i]) - ordOffset) if i < len(num2) and i >= 0 else 0
            singleRes = n1 + n2 + carry
            # print(singleRes)

            if singleRes >= 10:
                res +=  str(((singleRes / 10.0) - int(singleRes / 10)) * 10)[0]
                carry = int(singleRes / 10)
            else:
                res += str(singleRes)
                carry = 0

        if carry == 1:
            res += "1"
        return res[::-1]


s = Solution()
n1 = "237"
n2 = "284"
print(s.addStrings(n1, n2))
                





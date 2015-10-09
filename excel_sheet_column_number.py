class Solution(object):
        def titleToNumber(self, s):
        d = {}
        d['A'] = 1
        d['B'] = 2
        d['C'] = 3
        d['D'] = 4
        d['E'] = 5
        d['F'] = 6
        d['G'] = 7
        d['H'] = 8
        d['I'] = 9
        d['J'] = 10
        d['K'] = 11
        d['L'] = 12
        d['M'] = 13
        d['N'] = 14
        d['O'] = 15
        d['P'] = 16
        d['Q'] = 17
        d['R'] = 18
        d['S'] = 19
        d['T'] = 20
        d['U'] = 21
        d['V'] = 22
        d['W'] = 23
        d['X'] = 24
        d['Y'] = 25
        d['Z'] = 26
        pow = 0
        val = 0
        for i in range(len(s)-1, -1, -1):
            val += d[s[i]]*(26**pow)
            pow += 1
        return val
            

        
        

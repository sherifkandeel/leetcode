class Solution(object):
    def groupAnagrams(self, words):
        d = {}
        for word in words:
            sword = ''.join(sorted(word))
            if sword in d:
                d[sword].append(word)
            else:
                d[sword] = [word]
        
        grouped_anagrams = []
        for k, v in d.items():
            grouped_anagrams.append(sorted(v))
        
        return sorted(grouped_anagrams)
        
       
        

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

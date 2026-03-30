class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0 
        p2 = 0
        res = ""
        while p1 <= len(word1) - 1 and p2 <= len(word2) - 1:
            res += word1[p1] 
            p1 += 1
            res += word2[p2]
            p2 += 1
        
        if p1 <= len(word1) - 1:
            res += word1[p1:]
        
        elif p2 <= len(word2) - 1:
            res += word2[p2:]

        return res
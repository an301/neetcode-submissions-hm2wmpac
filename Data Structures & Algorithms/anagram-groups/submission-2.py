class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            reslist = [0] * 26
            for char in word:
                reslist[ord(char) - 97] += 1
            reslist = tuple(reslist)
            if reslist not in res:
                res[reslist] = []
            res[reslist].append(word)
        
        out = []
        for value in res.values():
            out.append(value)
        
        return out
        


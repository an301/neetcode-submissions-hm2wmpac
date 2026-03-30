class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord("a")] += 1
            key = tuple(key)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return res.values()



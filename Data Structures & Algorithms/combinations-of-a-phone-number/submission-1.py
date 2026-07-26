class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {"2":['a','b','c'],
                 "3":['d','e','f'],
                 "4":['g','h','i'],
                 "5":['j','k','l'],
                 "6":['m','n','o'],
                 "7":['p','q','r','s'],
                 "8":['t','u','v'],
                 "9":['w','x','y','z'],}

        result = []

        def helper(idx, curr):
            if idx == len(digits):
                result.append("".join(curr))
                return
            
            for letter in phone[digits[idx]]:
                curr.append(letter)
                helper(idx + 1, curr)
                curr.pop()
            

        helper(0, [])
        return result
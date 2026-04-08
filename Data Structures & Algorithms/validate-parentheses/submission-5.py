class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        mapped = {')':'(','}':'{',']':'['}
        for char in s:
            if char in mapped:
                if stack and stack[-1] == mapped[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
    

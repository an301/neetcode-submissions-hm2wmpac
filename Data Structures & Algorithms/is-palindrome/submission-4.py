class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1
            while right > left and not self.isValid(s[right]):
                right -= 1
            if s[right].lower() == s[left].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
    
    def isValid(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

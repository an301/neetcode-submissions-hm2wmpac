class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        edited = path.split('/')
        for fldr in edited:
            if fldr == '':
                continue
            if fldr != '.' and fldr != '..':
                stack.append("/"+fldr)
            elif fldr == '..':
                if stack:
                    stack.pop()
                
        if len(stack) == 0:
            return '/'
        else:
            ans = ''.join(stack)
            return ans
            
        
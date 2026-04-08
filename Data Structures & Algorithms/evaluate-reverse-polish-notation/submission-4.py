class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for char in tokens:
            if char not in ['+','-','*','/']:
                stack.append(char)
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if char == '+':
                    num = n2 + n1
                elif char == '-':
                    num = n1 - n2
                elif char == '*':
                    num = n2 * n1
                else:
                    num = int(n1 / n2)
                stack.append(num)
        return stack[0]
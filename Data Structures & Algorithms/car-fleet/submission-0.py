class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))

        stack = []
        for pair in reversed(pairs):
            if not stack:
                stack.append(pair)
            
            stack_time = (target - stack[-1][0])/float(stack[-1][1])
            curr_time = (target - pair[0])/float(pair[1])

            if curr_time > stack_time:
                stack.append(pair)

        return len(stack)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        to_remove = set()
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                right.append((asteroids[i],i))
            else:
                if right:
                    curr = len(right) - 1
                    while curr >= 0 and abs(asteroids[i]) > right[curr][0]:
                        to_remove.add(right[-1][1])
                        right.pop()
                        curr -= 1
                    if len(right) == 0:
                        continue
                    if abs(asteroids[i]) == right[-1][0]:
                        to_remove.add(right[-1][1])
                        to_remove.add(i)
                        right.pop()
                    elif abs(asteroids[i]) < right[-1][0]:
                        to_remove.add(i)
        
        out = []
        for i in range(len(asteroids)):
            if i not in to_remove:
                out.append(asteroids[i])

        return(out)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1dict = {}
        for char in s1:
            s1dict[char] = s1dict.get(char, 0) + 1

        state = {}
        start = 0
        for end in range(len(s2)):
            state[s2[end]] = state.get(s2[end], 0) + 1
            if end - start + 1 == n:
                if state == s1dict:
                    return True
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1

        return False

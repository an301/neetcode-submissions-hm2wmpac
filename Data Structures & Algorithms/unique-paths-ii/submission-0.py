class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)    #rows
        n = len(obstacleGrid[0]) #cols
        dp = [0] * n
        dp[n-1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
                # else:
                #     dp[c] = dp[c] + 0
        
        return dp[0]


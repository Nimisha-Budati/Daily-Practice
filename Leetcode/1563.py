#1563.Stone Game V(getting time limit exceed error)
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+stoneValue[i]
        dp=[[0]*n for _ in range(n)]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                for k in range(i,j):
                    left=prefix[k+1]-prefix[i]
                    right=prefix[j+1]-prefix[k+1]
                    if left<right:
                        dp[i][j]=max(dp[i][j],left+dp[i][k])
                    elif right<left:
                        dp[i][j]=max(dp[i][j],right+dp[k+1][j])
                    else:
                        dp[i][j]=max(dp[i][j],left+max(dp[i][k],dp[k+1][j]))
        return dp[0][n- 1]
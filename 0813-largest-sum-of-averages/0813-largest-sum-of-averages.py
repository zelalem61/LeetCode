class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N = len(nums)
        dp = [[0] * N for _ in range(k)] # k * N dp
        subtotal = 0
        for i in range(N - k + 1): # 5 -> 3
            subtotal += nums[i]
            dp[0][i] = subtotal / (i + 1)
        
        for r in range(1, k): # update each row in the order
            right = N - (k - r - 1) # leave k - r number of elements at the end of each row
            for j in range(r, right): # for each column
                subtotal = 0

                # update with max for the additional subaray + previously formed subarray
                for c in range(j, right): 
                    subtotal += nums[c]
                    dp[r][c] = max(dp[r][c], dp[r - 1][j - 1] + subtotal / (c - j + 1))

        return dp[k - 1][-1]
        
        
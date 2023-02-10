class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        L = (2**p - 2) // 2
        R = 2**p - 2
        ans = pow(R, L, MOD) * (2**p - 1)
        ans = ans % MOD
        return ans
        
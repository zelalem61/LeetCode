class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return 0
        while(n!=1):
            if n % 3 == 0:
                n = n // 3
            else:
                break
        return 1 if n == 1 else 0
    
        
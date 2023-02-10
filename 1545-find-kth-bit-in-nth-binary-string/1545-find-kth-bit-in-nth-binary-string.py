class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while n > 1:
            right = [('1' if c == '0' else '0') for c in s[::-1]]
            s = s + '1' + "".join(right)
            n -= 1
        return s[k-1]
        
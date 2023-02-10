class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n%4 != 0 and n!=1:
            return False

        division = n
        while division >= 4:
            division = division/4

        return division == 1
        
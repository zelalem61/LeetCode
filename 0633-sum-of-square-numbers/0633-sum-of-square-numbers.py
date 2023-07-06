class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)

        while i <= j:
            sum_squares = i*i + j*j

            if sum_squares == c:
                return True
            elif sum_squares < c:
                i += 1
            else:
                j -= 1

        return False

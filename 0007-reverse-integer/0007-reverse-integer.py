class Solution:
    def reverse(self, x: int) -> int:
        negative  = False
        if x < 0:
            negative = True
            x = -1 * x
        ans = ""
        stri = str(x)
        n = len(stri)
        leadingZero = True
        for i in range(n-1,-1,-1):
            if stri[i] != 0:
                leadingZero = False
            if leadingZero and atri[i] == 0:
                continue
            else:
                ans = ans+stri[i]
        
        if negative:
            result = int(ans) * -1
            if result < -1*(2**31) or result > (2**31)-1:
                return 0
            return result
        else:
            result = int(ans)
            if result < -1*(2**31) or result > (2**31)-1:
                return 0
            return result
       
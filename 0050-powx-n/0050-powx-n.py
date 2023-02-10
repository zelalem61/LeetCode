class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        power=1
        init=x
        while(power<n):
            x=x*x
            power=power*2
        if(power==n):
            return x
        z=self.myPow(init,power-n)
        if(math.isnan(z)):
            return 0
        return x/z
        
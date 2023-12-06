class Solution:
    def totalMoney(self, n: int) -> int:
        a = n//7
        fir = a+1
        rem = n % 7
        ans = 0
        summ = 28
        for i in range(a):
            ans = ans + summ + i*7
        for j in range(rem):
            ans += fir
            fir += 1
        return ans









            
#         while i < a:
#             for j in range(1,8):
#                 ans+=j+i
#             i+=1
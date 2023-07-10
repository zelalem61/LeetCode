class Solution:
    def totalFruit(self, fruits):
        y = -1
        z = -1
        count = 0
        maxi = float('-inf')
        y = fruits[0]
        for i in range(len(fruits)):
            if z == -1 and y == fruits[i]:
                count += 1
            elif z == -1 and y != fruits[i]:
                z = fruits[i]
                count += 1
            elif z == fruits[i]:
                count += 1
            elif y == fruits[i]:
                count += 1
            else:
                maxi = max(count, maxi)
                count = 1
                j = i - 1
                while fruits[j] == fruits[i - 1] and j >= 0:
                    count += 1
                    j -= 1
                z = fruits[i]
                y = fruits[i - 1]
        maxi = max(count, maxi)
        return maxi

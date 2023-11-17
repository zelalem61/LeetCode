class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = ["ans"] * len(score)
        
        athletes_score = sorted(score)[::-1]
        for i in range(len(athletes_score)):
            if i == 0:
                index = score.index(athletes_score[i])
                ans[index] = "Gold Medal"
            if i == 1:
                index = score.index(athletes_score[i])
                ans[index] = "Silver Medal"
            if i == 2:
                index = score.index(athletes_score[i])
                ans[index] = "Bronze Medal"
            elif i > 2:
                index = score.index(athletes_score[i])
                ans[index] = str(i+1)
        return ans
                
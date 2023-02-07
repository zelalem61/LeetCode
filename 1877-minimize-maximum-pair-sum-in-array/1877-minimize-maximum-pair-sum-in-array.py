class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        m=0
        for i in range(0,len(nums)):
            k=nums[i]+nums[-i-1]
            m=max(k,m)
        return m
        
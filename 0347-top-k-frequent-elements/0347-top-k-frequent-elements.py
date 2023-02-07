class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return 0
        nums = collections.Counter(nums)

        nums = sorted(nums.items(), key=lambda p:p[1], reverse=True)
        res = []
        for i in range(k):
            res += nums[i][0],
        return res
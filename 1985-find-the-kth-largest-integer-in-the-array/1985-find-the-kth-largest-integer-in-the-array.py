class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(i) for i in nums]
        nums.sort(reverse=True)
        return str(nums[k-1])
        
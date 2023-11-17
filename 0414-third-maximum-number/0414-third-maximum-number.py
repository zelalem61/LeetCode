class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinict_nums = sorted(set(nums))[::-1]
        
        if len(distinict_nums) >= 3:
            return distinict_nums[2]
        return distinict_nums[0]
        
        
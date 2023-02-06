class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        while True:
            swaps = 0
            for i in range(1, n-1):
                if nums[i-1] + nums[i+1] == 2*nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swaps += 1
                
            if swaps == 0:
                break
                
        return nums
        
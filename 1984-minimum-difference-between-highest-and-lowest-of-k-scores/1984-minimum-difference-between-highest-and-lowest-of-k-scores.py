class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float("inf")
        if k == 1:
            return 0
        else:
            i = 0
            j = k -1
            
            while j < len(nums):
                ans = min(ans, (nums[j] - nums[i]))
                i, j = i + 1, j + 1
               
            return ans
                    
            
            
            
        
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                nums[count] = i
                count += 1
        return nums[0:count]
        
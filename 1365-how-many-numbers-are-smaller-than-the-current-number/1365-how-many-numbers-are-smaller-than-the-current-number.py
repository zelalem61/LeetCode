class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temparr = nums.copy()
        result  = []
        nums.sort()
        for i in temparr:
            result.append(nums.index(i))
        return result
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arithmetic(nums: List[int]) -> bool:
            nums = sorted(nums)
            factor = nums[1]- nums[0]
            for j in range(len(nums)-1):
                if nums[j+1]-nums[j] != factor:
                    return False
            return True 
        answer = list()
        for left, right in zip(l, r):
            answer.append(arithmetic(nums[ left: right+1]))
        return answer
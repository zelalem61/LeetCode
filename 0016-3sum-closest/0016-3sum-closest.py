class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array

        result = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                if sums == target:
                    return target

                if abs(sums - target) < abs(result - target):
                    result = sums

                if sums < target:
                    j += 1
                else:
                    k -= 1

        return result

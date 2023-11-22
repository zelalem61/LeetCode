class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for_sum = []
        rev_sum = []
        
        sums = nums[0]
        for i in range(len(nums)):
            if i == 0:
                for_sum.append(sums)
            else:
                sums = sums + nums[i]
                for_sum.append(sums)
        ne_sum = nums[len(nums)-1]
        for j in range(len(nums)-1,-1,-1):
            rev_sum.append(ne_sum)
            ne_sum = ne_sum + nums[j-1]
        rev_sum = rev_sum[::-1]
        
        for k in range(len(nums)):
            if for_sum[k] == rev_sum[k]:
                return k
        return -1
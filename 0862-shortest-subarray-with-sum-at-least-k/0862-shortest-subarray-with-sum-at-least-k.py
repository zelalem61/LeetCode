class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1 
        shortest =float('inf')
        n = len(nums)
        presum =[0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        
        q = collections.deque()
        for i in range(n+1):
            while q and presum[q[-1]] >= presum[i]:
                q.pop()
            while q and presum[i] -presum[q[0]]>=k:
                shortest = min(shortest, i-q[0])
                q.popleft()
            q.append(i)
        if shortest ==float('inf'):
            return -1 
        return shortest
        
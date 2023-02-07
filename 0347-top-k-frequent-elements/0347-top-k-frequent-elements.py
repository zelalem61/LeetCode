class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        ctr = Counter(nums)
        common = ctr.most_common(k)
        for c in common:
            output.append(c[0])
        return output
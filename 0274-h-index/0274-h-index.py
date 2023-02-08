class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for x, num in enumerate(citations):
            if n-x <= num:
                return n-x
        return 0    
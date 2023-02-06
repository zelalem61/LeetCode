class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals) == 0:
            return ans
        intervals.sort()
        temp_interval = intervals[0]
        for i in intervals:
            if i[0] <= temp_interval[1]:
                temp_interval[1] = max(i[1], temp_interval[1])
            else:
                ans.append(temp_interval)
                temp_interval = i
        ans.append(temp_interval)
        return ans
        
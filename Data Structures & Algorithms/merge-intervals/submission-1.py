class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            curr = intervals[i]
            last = res[-1]
            if last[-1] >= curr[0]:
                last[-1] = max(last[-1], curr[-1])
            else:
                res.append(curr)
        return res
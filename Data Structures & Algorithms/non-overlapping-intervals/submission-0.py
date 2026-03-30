class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0        

        intervals.sort(key=lambda x: x[-1])
        res = [intervals[0]]

        for i in range(len(intervals)):
            curr = intervals[i]
            last = res[-1]
            if last[-1] <= curr[0] :
                res.append(curr)
            else:
                pass
        
        return len(intervals) - len(res)
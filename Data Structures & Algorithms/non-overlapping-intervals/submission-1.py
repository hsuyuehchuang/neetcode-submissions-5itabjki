
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        if not intervals:
            return count      

        intervals.sort(key=lambda x: x[-1])
        lastEnd = intervals[0][-1]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if lastEnd <= curr[0] :
                lastEnd = curr[-1]
            else:
                count+=1
        
        return count
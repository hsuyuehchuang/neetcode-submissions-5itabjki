class MedianFinder:

    def __init__(self):
        # two heap, small is small (maxheap), large is large (minheap)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # heapq.heappop()
        # heapq.heappush()
        # default heapq is minheap
        # max heap should add with -1*num
        heapq.heappush(self.small, -1 * num)

        # -1 * self.small[0]

        # make sure every num in small is <= every num is large
        # [1, 2, 3] [4] -> [1, 3] [2, 4]
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # [1, 2, 3] [4] -> [1, 2] [3, 4]
        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # [1], [2, 3, 4] -> [1, 2] [3, 4]
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2



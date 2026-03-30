class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        return self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        length = len(self.data)

        if not self.data:
            return None
        elif length == 1:
            return self.data[0]
        elif length % 2 == 0:
            return (self.data[length//2] + self.data[length//2 - 1]) / 2
        else:
            return self.data[int((length-1)/2)]
class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        left, right = 0, len(self.arr)
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid
        self.arr.insert(left, num)

    def findMedian(self) -> float:
        length = len(self.arr)
        mid = length // 2
        if length % 2 == 0:
            return (self.arr[mid - 1] + self.arr[mid]) / 2
        else:
            return self.arr[mid]

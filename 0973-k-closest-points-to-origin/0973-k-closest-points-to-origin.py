class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        heapq.heapify(l)
        for i in points:
            length=math.sqrt(i[0]*i[0]+i[1]*i[1])
            heapq.heappush(l,[length,i[0],i[1]])
        result=[]
        for i in range(k):
            dis,x1,y1=heapq.heappop(l)
            result.append([x1,y1])
        return result
        
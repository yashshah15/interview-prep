from heapq import heapify, heappush, heappop 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        minHeap=[]
        for row in range(min(n,k)):
            minHeap.append((matrix[row][0], row, 0))
        
        heapify(minHeap)
        res = 0
        for i in range(k):
            element, r, c = heappop(minHeap)
            
            # If we have any new elements in the current row, add them
            if c < n - 1:
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        
        return element
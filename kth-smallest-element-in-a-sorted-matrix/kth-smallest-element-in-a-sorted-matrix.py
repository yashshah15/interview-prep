from heapq import heapify, heappush, heappop 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        minHeap=[]
        #Choose only the minimum of n or k rows to save space
        for row in range(min(n,k)):
            minHeap.append((matrix[row][0], row, 0))
        #Create a min heap with row and column number also a par of heap tree node
        heapify(minHeap)
        res = 0
        for i in range(k):
            #extract min
            element, r, c = heappop(minHeap)
            
            # If we have any new elements in the current row, add them
            if c < n - 1:
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        
        return element
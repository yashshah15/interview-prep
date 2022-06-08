#Greedy + 2 pointer approach
# Initialize two pointers at the opposite ends of the array. Greedily choose the pointer pointing to a greater heighht.
# Calculate the area as you move the pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left  = 0
        right = len(height) - 1
        
        while(left < right):
            max_area = max(max_area, min(height[left],height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            
            else:
                right -=1
        
        return max_area
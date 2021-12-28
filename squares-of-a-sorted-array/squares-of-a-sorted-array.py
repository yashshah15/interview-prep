class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #two pointer approach for this problem. We have to check the negative part and positive part of the array. The one with the lower absolute value will be first included in the result. 
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) >= nums[right]:
                element = nums[left]
                left += 1
            
            else:
                element = nums[right]
                right -= 1
            
            result[i] = element * element
        
        return result
            
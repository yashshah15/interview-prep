class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #This is similar to the local maxima problem
        
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return 0
        
        while left < right:
            mid = left + (right - left) // 2
            
            #if mid element is grater than both its neighbouring elements
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            
            elif nums[mid] > nums[mid + 1]:
                right = mid
            
            else:
                left = mid + 1
            
            
        return left if nums[left] >= nums[right] else right
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        #Last element is greater than the first element then the smallest elemnent is at index 0
        if nums[right] > nums[left]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            
            #if mid element is grreater than its next element, then mid +1 is the smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1] 
            
            #if mid element is smaller than its previous element then mid is the smallest element
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            #if middle element is greater than first element, we need to check in the right subarray
            if nums[mid] > nums[left]:
                left = mid + 1
            #else tbe element is present in left subarray
            else:
                right = mid - 1
                
            
        
        
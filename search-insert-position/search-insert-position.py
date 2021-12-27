class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg = 0 
        end = len(nums) - 1
        mid = (beg + end) // 2
        
        while nums[mid] != target and beg <= end:
            if target >= nums[mid]:
                beg = mid + 1
            
            else:
                end = mid - 1
            
            mid = beg + (end - beg) // 2 
        
        if target == nums[mid]:
            return mid
         
        else:
            if target > nums[mid]:
                return mid + 1
            
            else:
                return mid if mid>0 else 0
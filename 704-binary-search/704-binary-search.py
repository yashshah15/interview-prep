class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1
        mid = (beg + end) // 2
        
        while target != nums[mid] and beg <= end:
            if target <= nums[mid]:
                end  = mid - 1
            
            else:
                beg = mid + 1
            
            mid = (beg + end) // 2
        
        if target == nums[mid]:
            return mid
        
        else:
            return - 1 
            
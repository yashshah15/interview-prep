class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1
        mid = (beg + end) // 2

        
        while nums[mid] != target and beg <= end:
            #array from beg to mid is not rotated
            if nums[mid] >= nums[beg]:
                #check if the array lies in this half
                if target >= nums[beg] and target <= nums[mid]:
                    end  = mid - 1
                #target may exist in the other half
                else:
                    beg = mid + 1
            #Situation where athe array from beg to end is rotated
            elif nums[mid] <= nums[beg]:
                if target >= nums[mid] and target <= nums[end]:
                    beg = mid + 1
                
                else:
                    end = mid - 1
            
            mid = (beg + end) // 2
        
        if nums[mid] == target:
            return mid
        
        else:
            return - 1
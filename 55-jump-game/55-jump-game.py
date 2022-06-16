class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reachable_index=0
        for i in range(0,len(nums)):
            if max_reachable_index <i:
                return False
            if max_reachable_index <= i + nums[i]:
                max_reachable_index = i + nums[i]
                
        return True
        
        
            
        
        
    
        
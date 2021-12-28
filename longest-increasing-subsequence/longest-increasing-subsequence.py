class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        opt =[1] * n
        
        
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    opt[i] = max(opt[i], opt[j] + 1)
        
                
                
        
        return max(opt)
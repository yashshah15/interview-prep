class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        
        for i in range(2,len(nums)):
            
            if dp[i-2] + nums[i] > dp[i-1]:
                dp[i]=dp[i-2] + nums[i]
                i=i+2
            else:
                dp[i] = dp[i-1]
                i=i+1
            print(dp)
        return(dp[-1])
        
        
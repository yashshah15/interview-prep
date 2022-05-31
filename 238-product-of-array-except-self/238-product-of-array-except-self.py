class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        n = len(nums)
        right  = [1] * (n)
        for i in range(1, n):
            left.append(left[i-1] * nums[i-1])
        
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        print(left, right)
        res = []
        
        for i in range(n):
            res.append(left[i]*right[i])
        
        return res
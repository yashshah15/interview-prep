#O(1) Space solution
#Calculate prefix product from left to right and use a variable to store the suffix product.
#Calculate the result from right to left updating the right variable as suffix product 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        right  = 1
        
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        for i in range(n-1, -1, -1):
            res[i] = right * res[i]
            right = right * nums[i]
        
        return res
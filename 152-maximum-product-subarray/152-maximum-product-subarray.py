class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        max_product=nums[0]
        min_product=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            temp_max_product=max(nums[i],max_product*nums[i],min_product*nums[i])
            min_product=min(nums[i],max_product*nums[i],min_product*nums[i])
            max_product=temp_max_product
            res=max(res,max_product)
            #print(max_product,min_product, res)
        return res
    
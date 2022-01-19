class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k % n == 0:
            return nums
        
        elif k > n:
            k = k % n
        
        
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
        
        return nums
            
        
        
            
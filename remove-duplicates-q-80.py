class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        counter = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]: 
                if counter >= 1 : 
                    del nums[i]
                else : 
                    i += 1
                counter += 1
            else : 
                i += 1 
                counter = 0 
        return len(nums)
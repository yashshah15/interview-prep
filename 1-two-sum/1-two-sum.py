class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,n in enumerate(nums):
            remaining = target- n
            if remaining in seen:
                return [seen[remaining],i]
            else:
                seen[n]=i
        return []
            
        
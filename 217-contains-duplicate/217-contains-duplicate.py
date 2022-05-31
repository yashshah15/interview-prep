class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i, 0) == 0:
                d[i] = 1
            else:
                return True
        
        return False
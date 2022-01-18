class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        
        for i in count:
            if count[i] == degree:
                ans = min(ans, right[i] - left[i] + 1)
        #print(count)
        return ans
    
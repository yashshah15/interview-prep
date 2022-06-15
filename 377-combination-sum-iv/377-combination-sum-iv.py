class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        opt = [0] * (target + 1)
        opt[0] = 1
        
        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    opt[i] += opt[i - j]
        
        return opt[-1]
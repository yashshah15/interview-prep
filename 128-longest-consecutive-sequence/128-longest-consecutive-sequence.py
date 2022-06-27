class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)
        
        for i in nums:
            if i - 1 not in nums_set:
                sequence_start = i
                current_streak = 1
                
                while sequence_start + 1 in nums_set:
                    current_streak += 1
                    sequence_start += 1
                    
                longest_streak = max(longest_streak, current_streak)
            
        
        return longest_streak
                    
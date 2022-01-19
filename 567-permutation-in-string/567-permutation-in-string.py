class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window approach
        #use counter to count the occurances of each item and move the sliding window to the right
        # The size of the sliding window is len(s2-21) + 1
        ctr1 = collections.Counter(s1)
        i = 0
        while i < len(s2) - len(s1) + 1:
            if s2[i] in ctr1:
                ctr2 = collections.Counter(s2[i: i+len(s1)])
                if ctr1 == ctr2: return True
            i += 1
        return False

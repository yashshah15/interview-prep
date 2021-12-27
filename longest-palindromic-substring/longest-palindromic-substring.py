class Solution:
    def expandFromCentre(self, s, left, right) -> int:
        if not s or left > right:
            return 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #to handle the case where string len is 1 and we are exanding pointers    
        return right - left - 1
    
        
        
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1: return ""
        
        start = 0
        end = 0
        for i in range(len(s)):
            #for case where substring has a unique char in the centre for eg aba
            len1 = self.expandFromCentre(s, i, i)
            #for the case where substring does not have unique char at centre eg abba  
            len2 = self.expandFromCentre(s, i, i+1)
            maxLength = max(len1, len2)
            #update the start and end pointers to denote the substring length
            if maxLength > end - start:
                start = i - (maxLength - 1)//2
                end = i + maxLength //2
        
        return s[start:end+1]
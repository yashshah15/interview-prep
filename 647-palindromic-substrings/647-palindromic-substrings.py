class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCentre(s, left, right):
            ans = 0
            
            while left >= 0 and right < len(s):
                #we ar eassuming that we have a palindrome string and we are adding wo characters at the two ends
                #if they are not equal we don't need to do anything as it is not palindrome
                if s[left] != s[right]:
                    break
                
                left -= 1
                right += 1
                ans += 1
            
            return ans
        ans = 0
        for i in range(len(s)):
            
            #for odd loength palindromes
            ans += expandAroundCentre(s, i, i)
            #for even length palindrome
            ans += expandAroundCentre(s, i, i + 1)
            
        
        return ans
        
        
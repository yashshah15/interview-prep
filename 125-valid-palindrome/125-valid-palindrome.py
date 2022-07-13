class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for c in s:
            if c.isalnum():
                st= st + c.lower()
        left = 0
        right = len(st)- 1
        
        while left < right:
            if st[left]  == st[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
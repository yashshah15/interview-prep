class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        
        if n%2 == 0:
            left = n//2 -1
            right = left + 1
        
        else:
            left = n//2 - 1
            right = left + 2
        
        while left >=0 and right<n:
            s[left], s[right] = s[right], s[left]
            left -= 1
            right += 1
        
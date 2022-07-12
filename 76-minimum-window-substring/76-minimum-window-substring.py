class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}
        l = 0
        res = [-1, -1]
        res_len = float("infinity")
        required = 0
        have = 0
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        required = len(countT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
        
            
            while have == required:
                #Compare window size
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                #Try shrinking window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r + 1] if res_len != float("infinity") else ""
                
            
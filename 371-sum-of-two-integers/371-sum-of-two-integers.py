class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = abs(a)
        y = abs(b)
        if x < y:
            return self.getSum(b, a)
            
        
        sign = 1 if a > 0 else -1
        
        if a*b > 0:
            #Performing addition
            
            while y:
                s = x ^ y
                c = (x & y) << 1
                x = s
                y = c
        
        else:
            #Perform subtraction 
            while y:
                s = x ^ y
                b = ((~x) & y) << 1
                x = s
                y = b
        
        return x * sign
            
        
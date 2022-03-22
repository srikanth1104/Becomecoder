import math
class Solution:
    def isPossible(self, x, y, a, b):
        k=math.gcd(a,b)
        m=math.gcd(x,y)
        if k==m:
            return 1
        else:
            return 0

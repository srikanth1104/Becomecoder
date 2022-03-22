import math
class Solution:
    def gcd(self, n, arr):
        i=0
        if len(arr)==1:
            return arr[0]
        r=arr[0]
        while i!=len(arr)-1:
            r=math.gcd(r,arr[i+1])
            i+=1
        return r

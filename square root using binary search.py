def sqrtN(n):
    s=1
    e=n
    mid=n//2
    while(s<=e):
        if mid*mid==n:
            return mid
        elif mid*mid>n:
            e=mid-1
            mid=(s+e)//2
        elif mid*mid<n:
            s=mid+1
            mid=(s+e)//2
    return mid   

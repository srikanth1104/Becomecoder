def recyclePens(n, r, k, c):
    l=1
    h=n
    while(l<=h):
        mid=(l+h)//2
        amnt=r+(n-mid)*k
        if(mid*c<=amnt):
            l=mid+1
        else:
            h=mid-1
    return h

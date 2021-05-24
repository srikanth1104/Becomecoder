def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)

a,b=map(int,input().split())
print(lcm(a,b,2))
    

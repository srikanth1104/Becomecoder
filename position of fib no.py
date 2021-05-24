def isfib(n):
    if n==0 or n==1:
        return True
    a=0
    b=1
    count=2
    while True:
        c=a+b
        count+=1
        if c==n:
            print(count)
            return True
        if c>n:
            return False
        a=b
        b=c
n=int(input())
print(isfib(n))

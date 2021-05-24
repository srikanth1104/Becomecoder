def disarium(num):
    c=0
    temp=num
    s=0
    while num:
        num//=10
        c+=1
    num=temp
    while temp:
        r=temp%10
        temp=temp//10
        s=s+pow(r,c)
        c-=1
    return s==num

    

num=int(input())
print(disarium(num))

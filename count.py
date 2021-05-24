num=int(input())
c=0
while num:
    r=num%10
    num=num//10
    c+=1
print(c)

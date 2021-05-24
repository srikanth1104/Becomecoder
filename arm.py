num=int(input())
s=c=0
temp=num
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
while num:
    r=num%10
    num=num//10
    s+=r**c
if s==temp:
    print("Armstrong number")
else:
    print("Not a armstrong number")

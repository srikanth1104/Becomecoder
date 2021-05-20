n=int(input())
s=0
c=0
temp=n
while n:
    r=n%10
    n=n//10
    c+=1
n=temp
while n:
    r=n%10
    n=n//10
    s+=r**c
if s==temp:
    print("Armstrong number")
else:
    print("Not a armstrong number")

    
    

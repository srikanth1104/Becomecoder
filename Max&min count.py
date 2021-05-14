#Max & Min count of a number
num=int(input())
temp=num
min=num%10
max=num%10
a=b=0
while num:
    r=num%10
    num=num//10
    if r>max:
        max=r
    if r<min:
        min=r
print(min,max)        
num=temp
while num:
    r=num%10
    num=num//10
    if r==min:
        a+=1
    if r==max:
        b+=1
print(a,b)        

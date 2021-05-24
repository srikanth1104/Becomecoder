num,r1,r2=map(int,input().split())
i=r1
if r1>r2:
     print(num," x ",i," = ",num*i)
    i+=1
    
while i<=r2:
    print(num," x ",i," = ",num*i)
    i+=1

num,r1,r2=map(int,input().split())
for i in range(1,r2+1):
    if (num*i)%r1!=0:
        print(num," x ",i," = ",num*i)
    

def ispronic(num):
    for i in range(num):
        if i*(i+1)==num:
            return True
    return False    

num=int(input())
print(ispronic(num))

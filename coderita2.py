n=int(input())
for _ in range(n):
    a=int(input())
    b=list(map(int,input().split())) # 1 5 3 4
    i=1
    j=1
    co=1
    while True:
        c=b[i]-j
        co+=1
        if c<=0:
            break
        i+=1
        j+=1
        if c!=0 and i==len(b):
            i=0
    if co<len(b):
        print(co)
    else:
        print(len(b)//co+1)
        

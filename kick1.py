t=int(input())
for X in range(1,t+1):
    N=int(input())
    L=list(map(int,input().split()))
    g=1
    Y=0
    while g<len(L)-1:
        if L[g]>L[g-1] and L[g]>L[g+1]:
            Y+=1
        g+=1
    print("Case #"+str(X)+":"+" "+str(Y))    

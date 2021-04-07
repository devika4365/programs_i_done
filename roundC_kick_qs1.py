T=int(input())
for i in range(1,T+1):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    c=0
    g=[]
    for h in range(len(L)-1):
        if L[h]-1==L[h+1]:
            g.append(L[h])
            if L[h+1]==1 and len(g)>=K-1:
                c+=1   
        else:
            g=[]
    print("Case #"+str(i)+":"+" "+str(c))     

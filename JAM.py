t=int(input())
for i in range(1,t+1):
    N,K=map(int,input().split())
    mainl=[]
    for h in range(N):
        g=list(map(int,input().split()))
        mainl.append(g)
    s=0  
    f=0
    p=mainl[0][0]
    for b in range(len(mainl)):
        l=mainl[b][b]
        if l==p:
            s=s+l
        else:
            f=1
            break
    if s==K:
        mk=[]
        for v in range(len(mainl)):
            d=mainl[v]
            for x in range(len(mainl)):
                mk.append(mainl[x][v])
            h=d[v]
            if d.count(h)==1 and mk.count(h)==1:
                mk=[]
            else:
                f=1
                break
        if f==0:
            print("Case #",i,": POSSIBLE")
    else:
        print("Case #",i,": IMPOSSIBLE")
                
            
                
            
            
            
            
        

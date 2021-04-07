T=int(input())
for i in range(1,T+1):
    N=int(input())
    L=list(map(int,input().split()))
    c=0
    for j in range(len(L)):
        h=[]
        for k in range(j,len(L)):
            h.append(L[k])
            s=sum(h)
            b=s**(1/2)
            if b%1==0:
                c+=1
    print("Case #"+str(i)+":"+" "+str(c))                
        
        
        
    

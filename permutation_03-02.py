n=list(map(int,input().split()))
ty=sorted(n)
tu=ty[::-1]
if n==ty:
    temp=n[-1]
    n[-1]=n[-2]
    n[-2]=temp
    print(n)
elif n==tu:
    print(n)
else:
    pp=[]
    for i in range(len(n)):
        pp.append(n[i])
        j=n[i]
        t=[]
        f=n.index(j)
        l=n[i+1:]
        #print(l,"l list")
        y=sorted(l)
        h=list(y)
        #print(h,"h value")
        g=h[::-1]
        #print(g,"g value")
        if i==0 and l==h:
            print(n)
            break
        elif(l==h):
            temp=n[-1]
            n[-1]=n[-2]
            n[-2]=temp
            print(n)
            break
        elif l==g:
            for k in l:
                if k>j:
                    t.append(k)
            minimum=min(t)
            v=l.index(minimum)
            cc=n.index(minimum)
            n[cc]=j
            n[f]=minimum
            l[v]=j
            #print(n,t,l)
            mm=l[i+1::-1]
            jj=n[0:i+1]
            jj.extend(mm)
            print(jj)
            break
    
                
        
           
        
                
                
        

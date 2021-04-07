for _ in range(int(input())):
    s=input()
    c=0
    d=0
    u=[]
    m=0
    for i in s:
        p=s.count(i)
        #print(p)
        if p>=c:
            #c=p
            if p==c:
                u.append(i)
                x=ord(i)
                if x>d:
                    d=x
                    t=i
            elif p>c:
                u=[]
                u.append(i)
            c=p
            t=i
            #print(c,t)
            #print(u)      
    for z in u:
        if ord(z)>m:
            y=z
            m=ord(z)
    print(y,c)        
                    
                
            
        
    #print(t,p)            

m=list(map(int,input().split())) # 6 3 5 4 3 2
for i in range (len(m)-1): # 0-4
    s=m[0:i+1] # 6
    print(s)
    k=m[i+1:] # 3 5 4 3 2
    print(k)
    c=0
    d=0
    for j in range(len(k)):
        if j==len(k)-1:
            break
         #print("loop")
        if k[j]>k[j+1]:# 3>5
            c+=1 #0
            #print(c,"cccc")
           
        elif k[j]<k[j+1]: 
            d+=1
    if c==len(k)-1:
        #print("descending")
        if i==0:
            print(m)
            break
        else:       #1
            g=m.index(m[i])
            p=m[i]#2 index
            for f in k:
                if f==k[i]+1:
                    h=m.index(f)# 5
                    e=k.index(f)# 2
            rr=f 
            m[g]=f
            m[h]=p
            k[e]=p
            
            k=k[::-1]
            s=s+k 
    elif d==len(k)-1:
        temp=m[-1]
        m[-1]=m[-2]
        m[-2]=temp
        s=s+k
        
        
        
print(s)

        
            
            
            
            
                    
        
        
       
            
            
    
    
    
    







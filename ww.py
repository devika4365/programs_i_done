s=input() #3[a2[c]]
k=[]
p=''
r=''
c=0
for i in s:
    if i!=']':
        k.append(i)
        #print(k)   
    elif i==']':
        v=k.pop()
        if v!='[':
            p+=v
            print(p,'p')
        elif v=='[': # [
            c+=1
            u=k.pop()
            u=int(u)
            print(u,'u')
            e=p*u
            print(e,p,u)
            if c==1:
                k.append(e)
                print(k)
                break
                
        r+=p
    p=''
        
            
            
            
            
            
            
            
        
        
        
     
    
    
    

s1=input()#abcd
s2=input()#a*c_
i=0
p=1
j=0

while i<len(s2):
    if s2[i]==s1[i] or s2=='_':
        i+=1
        continue
    elif s2[i]=='*':
        if (i==len(s2)-1):
            print("follows")
            break
        i+=1
        k=s1[::-1]
        u=0
        for h in k:
            if s2[i]==h:
                f=k.index(h)
                f=f-((2*f)+1)
                i+=1
                u=1
                break
        if u==0:
            print("not follows")
            break
        elif u==1:
            if s2[i-1]==s1[f+1] or s2[i]=='_':
                i+=1
                continue
            else:
                print("not ;;;")
                break
        elif(i==len(s2)-1):
            print("follows")
            
                    
                
        
        
            
            
            
    i+=1    
        
    

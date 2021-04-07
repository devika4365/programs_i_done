s=input()
u=''
c=0
i=0
v=0
while i<len(s):
    c+=1
    u+=s[i]
    #print(u,'u')
    if c==4:
        u+=':'
        u+='//'
    if v==0 and (s[i+2]=='u' and s[i+1]=='r') :
        v+=1
        u+='.'
    if v==1 and s[i]=='u' and s[i-1]=='r':
        u+='/'
        v+=1
    i+=1
print(u)        
        
            
    
    

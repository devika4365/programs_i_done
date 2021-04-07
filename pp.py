s=input()
c=0
i=0
t=0
p=0
while i<len(s):
    if ord(s[i])==40:
        c+=1
    elif ord(s[i])==41:
        if i==0:
            t=0
        else:
            t+=1
    #print(c,t,"c,t")    
    if t>0 and c>0:
        c-=1
        t-=1
        p+=1
    elif t>c:
        r=t-c
        t=t-r
        #print(c,t)
       # print(p,"p")
    i+=1
print(p)    
            

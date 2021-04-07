l=input()
d=input()
k=list(d)
j=len(l)-len(d)
y=''
m=0
for w in d:
    if w=='*':
        q=k.index('*')
        k.pop(q)
        for h in range(j+1):
            k.insert(q,'_')
for t in k:
    y+=t
print(y)    
i=0        
while i<len(y) :
    if l[i]=="_":
        i+=1
        continue
    elif y[i]=='_':
        i+=1
        if i<len(l) and i<len(y):
            continue
        else:
            m=1
            break
    elif l[i]!=y[i]:
        m=1
        break
    i+=1

if m==0:
    print("follows")
else:
    print("not follows")
    


    
        
        
    


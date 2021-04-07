n=input()
v=list(n)
g=[]
for h in range(len(v)):
    if (ord(v[h])>=97 and ord(v[h])<=122) or (ord(v[h])>=65 and ord(v[h])<=90):
        g.append(v[h])
        
g=g[::-1]
m=0
for h in range(len(v)):
    if (ord(v[h])>=97 and ord(v[h])<=122 ) or (ord(v[h])>=65 and ord(v[h])<=90):
        v[h]=g[m]
        m+=1
print(''.join(v))    
        
    


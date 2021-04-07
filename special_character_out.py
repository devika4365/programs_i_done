n=input()
v=list(n)
g=[]
d=[]
gg=[]
c=0
for i in range(len(v)):
    if v[i].isdigit():
        if int(v[i])%2==0:
            g.append(v[i])
        else:
            d.append(v[i])
    else:
        c+=1
v=len(g)+len(d)        
if c%2==0:
    #print("even count")
    u=0
    i=0
    for h in range(v):
        if h%2==0:
            #print(u,'u value')
            gg.append(g[u])
            #print(gg,"gg when even start")
            u+=1
        else:
            gg.append(d[i])
            #print(gg,'gg when odd start')
            i+=1
else:
    #print("odd count")
    u=0
    i=0
    for h in range(v):
        if h%2==0:
            gg.append(d[u])
            u+=1
        else:
            gg.append(g[i])
            i+=1
print(''.join(gg))            
    
            
        


s=input()
l=s.split()
print(l)
d={}
f=0
for i in l:
    j=l.count(i)
    if j>=f:
        if j==f:
            d[i]=j
        else:
            d={}
            d[i]=j
        f=j    
print(d)            
        

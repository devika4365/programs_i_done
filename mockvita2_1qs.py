n=input()
bride=input()
groom=input()
b=list(bride)
g=list(groom)
p=0
i=0
j=0
while i==0 and j==0 and b!=[]and p<len(bride):
    if b[i]==g[j]:
        b.pop(0)
        g.pop(0)
    else:
        k=g.pop(0)
        g.append(k)
        p+=1

print(len(b))
        

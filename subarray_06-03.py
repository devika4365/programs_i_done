n=int(input())
b=int(input())
l=[i for i in range(n,b+1)]
d=[l[i:j+1] for i in range(len(l)) for j in range(i,len(l))]
c=0
for j in d:
    if sum(j)%2!=0:
        c+=1
        

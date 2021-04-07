l=list(map(int,input().split()))
l=sorted(l)
j=[]
j.append(l[0])
j.append(l[1])
for i in range(2,len(l)):
    if j[i-1]+j[i-2] in l:
        j.append(j[i-1]+j[i-2] )
    else:
        break
print(j)    
        

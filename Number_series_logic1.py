num=int(input())
main=[1]
sub=[1]
i=1
j=0
k=0
while True:
    if (len(main)==num):
        break
    val=3*i
    if val%12!=0:
        q=sub[j]+val
        sub.append(q)
        r=sub[j]+main[k]
        main.append(r)
        j+=1
        k+=1
    i+=1
    
print(*main)    
        
        

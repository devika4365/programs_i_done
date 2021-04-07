t=int(input())
i=int(input())
l=[i for i in range(1,i+1)] #
u=[]
c=0
for i in range(len(l)): #len(l)--3( 1 2 3)   0
    for j in range(i,len(l)): # 0 2
        for k in range(i,j+1):
            u.append(l[k]) # 1
        # print(u)    
        if (sum(u))%2!=0:
            c+=1
        u=[]
print(c)
        
    

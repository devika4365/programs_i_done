n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
k=[]
for i in range(len(n1)):
    for j in range(len(n2)):
        if n1[i]==n2[j]:
            for h in range(j+1,len(n2)):
                if n2[h]>n1[i]:
                    k.append(n2[h])
                    break
                elif (h==len(n2)-1):
                    k.append(-1)
print(k)                    

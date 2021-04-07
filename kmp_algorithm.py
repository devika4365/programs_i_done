s=input()
op=input()
y=[]
t=[]
for h in range(len(op)):
    if  op[h] not in y:
        y.append(op[h])
        t.append(0)
    else:
        t.append(y.index(op[h])+1)
#print(t)


j=0
while True:
    for i in s:
        if i==op[j]:
            if j+1==len(op):
                print("found")
                break
            j+=1
        else:
            j=t[j]
            continue
    break    

            
        
    
        
        

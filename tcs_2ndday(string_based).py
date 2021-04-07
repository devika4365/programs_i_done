s=input()# abbac
c=0
high=[]
equal=[]
low=[]
for i in s:
    if i in equal:
        continue
    else:
        equal.append(i)
        low.append(s.count(i))
print(equal,low)
l=0
h=0
ss=low[0]
b=0
for j in range(len(low)-1):
    if low[j]==low[j+1] and l==0:
        h+=1
        continue
    elif low[j]<low[j+1] or low[j]>low[j+1]:
        f=abs(low[j]-low[j+1])
        if f>1:
            print("not valid")
            b=1
            break
        else:
            l+=1
            print("Lvalue",l)
        
    else:
        b=1
        print("not valid")
        break
        
if h==len(low):
    print("valid")
elif l==1 and b==0:
    print("make it valid")
print(b)    
    

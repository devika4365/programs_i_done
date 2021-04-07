n=(input())
st=''
for i in range(len(n)):
    if n[i]=="(":
        st+=(n[i::])
        break
a=list(st[::-1])
print(a)
l=[]
while True:
    for j in a:
        if j.isdigit():
            b=int(j)
            a.pop(a.index(str(b)))
            l.extend(b*a[::])
            break
    break
print(l)
        
        
    
    

        
 

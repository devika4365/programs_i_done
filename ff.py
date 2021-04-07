s=input()
s=s[::-1]
k=''
y=''
c=0
d=0
r=0
u=''
for i in s:
    if i==']':
        c+=1
    elif i=='[':
        d+=1
        if d==1 and c==1:
            r=1
            d=0
            c=0
    elif i.isalpha():
        k+=i
    elif i.isdigit():
        if r==1:
            y=k*int(i)
            k=''
            #print(y,'yyy')
            u+=y
            #print(u,'kkkkk')
            y=''
            if s.index(i)==len(s)-1:
                print(u[::-1],"hdsdsj")
        else:
            k=k*int(i)
            #print(k,'k')
    
print(k[::-1])        
    


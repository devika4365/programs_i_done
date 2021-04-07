n=input()
l=[]
m=[]
a=False
for i in n:
 if i.isdigit():
     if(int(i)%2)==0:
         a=True
         if str(i) in m:
             continue
         m.append(i)
     else:
         if str(i) in l:
             continue
         l.append(i)
#print(l,"odd")
#print(m)
if a:
    n=str(min(m))
    #print(n)
    m.remove(min(m))
    l.extend(m)
    #print(l)
s=''
while (len(l)>0) and a:
    s=s+str(max(l))
    #print(s,"s")
    l.remove(max(l))
if a:
    print(int(s+n))
else:
    print('-1')

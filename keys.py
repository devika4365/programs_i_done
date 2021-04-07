s=input()
d={}
for j in range(2,10):
    d[j]=[]
for h in d.keys():
    print(h)
    if h==7 or h==9:
         for t in range(4):
          d[h].append(input())
    else:
        for t in range(3):
          d[h].append(input())
print(d)
for f in s:
    for r in range(2,10):
        if f in d[r]:
            print(r,end='')
            q=d[r].index(f)+1
            if q!=1:
                print(q,end='')
            
    
      
      


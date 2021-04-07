column=int(input())
matrix=[]
for j in range(3):
    h=[]
    for i in range(column):
        h.append(input())
    matrix.append(h)    
A=['.','*','.','*','*','*','*','.','*']
E=['*','*','*','*','*','*','*','*','*']
I=['*','*','*','.','*','.','*','*','*']
O=['*','*','*','*','.','*','*','*','*']
U=['*','.','*','*','.','*','*','*','*']
s=''
while True:
    d=[]
    for g in range(3):
        for m in range(3):
            x=matrix[g].pop(m)
            d.append(x)
        #print(matrix[g])    
    if d==A:
        s+='A'
    elif d==E:
        s+='E'
    elif d==I:
        s+='I'
    elif d==O:
        s+='O'
    else:
        s+='U'
    if matrix==[]:
        break
    else:
        for b in range(3):
            c=matrix[b]
            c.pop(0)
        s+='#'
print(s)        
            
            
    

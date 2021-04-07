s=input() #3[a2[c]]
k=[]
p=''
w=''
for i in s:# 3 [ a 2 [ c ]
    if i!=']': 
        k.append(i) # 3 [ a 2 [ c
    elif i==']': # ]
        while len(k): #6
            v=k.pop() # c
            if v=='[':
                break # 1
            else:
                p+=v
        p=p[::-1]
        print(p,'p')
        g=k.pop()
        #print(g,'g')
        if g.isdigit():
            print(p)
            p=p*int(g)
            #print(p,'p')
            k.append(p)
            p=''
print(''.join(k))            

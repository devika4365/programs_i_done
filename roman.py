num=[1,5,10,50,100,500,1000]
al=['I','V','X','L','C','D','M']
s=input()
k=0
e=0
add=0
for i in range(len(s)):
    for j in range(len(al)):
        if i==0:
            g=al.index(s[i])
            add=add*1+num[g]
            e=g
            #print("adding if 0",add)
            break
        if s[i]==al[j]:
            g=al.index(s[i])
            #print(g,"g valiue")
            if g<=e:
                add=add*1+num[g]
                e=g
                #print(add,"add",e,"e val")
            else:
                n=num[g]-num[e]
                print(num[g],num[e])
                #print(n,"n value")
                add=(add*1+n)-num[e]
                #print(add,"else")
print(add)            

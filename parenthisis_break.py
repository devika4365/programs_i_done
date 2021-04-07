n=input() #))( #
l=[]
o=['(','[','{']
c=[')',']','}']
h=0
if n[0] in c:
    print(1)
else:
    for i in n:
        if i in o:
            l.append(i)
            print(l)
        elif i==")" or i=="]" or i=="}":
            #print(i,' closed parenthis')
            #print(l[-1])
            if (i==')' or i=='}' or i==']') and l==[]:
                j=n.index(i)
                h=1
                print(j+1)
                break
            elif (i==')' and l[-1]=='(') or (i==']' and l[-1]=='[') or (i=='}' and i=='{'):
                #print(i)
                #print(l[-1],"l[-1]")
                l.pop()
                #print(l)
            else:
                print(l,"l value")
                j=n.index(i)
                h=1
                print(j+1)
                break
      
    if l!=[] and h==0:
        print(len(n)+1)
    else:
        if h==0:
            print(0)
        

    

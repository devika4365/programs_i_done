b=input()
l=['1','0']
h=0
for i in b:
    if i not in l:
        #print(i)
        print("ERROR")
        h=1
        break
if h==0:
    print(int(b,2))
    
        
        

print("what is ur IP address")
ip=input()
l=ip.split('/')
ip_address=l[0].split('.')
hh=ip_address
ls=[]
for v in range(len(ip_address)):
    z=int(ip_address[v])
    ls.append(z)
print(ls)    
pre_len=int(l[1])
m=[]
main=[]
if int(ip_address[0])>=0 and int(ip_address[0])<=127:
    p=8
    print("class A")
    nb=pre_len-p
    hb=32-pre_len
    print("No.of Networks :",2**nb,nb)
    print("No.of Host :",(2**hb)-2,hb)
    i=0
    hh[-1]='0'
    for j in range(1,(2**nb)+1):
        for g in range(2**hb):
            m.append('.'.join(hh))
            i+=1
            hh[-1]=str(i)
            if i==256:
                ls[-2]=ls[-2]+1
                hh[-2]=str(ls[-2])
                i=0
            if ls[-2]==256:
                ls[-3]=ls[-3]+1
                hh[-3]=str(ls[-3])
                ls[-2]=0
        print("Network :",j)        
        print("Network ID :",m[0])
        print("Broadcast ID :",m[-1])
        print("usable ip's :",m[1],"-",m[-2])
        main.append(m)
        m=[]
        
        
            
            
    
elif int(ip_address[0])>=128 and int(ip_address[0])<=191:
    p=16
    print("class B")
    nb=pre_len-p
    hb=32-pre_len
    print("No.of Networks :",2**nb,nb)
    print("No.of Host :",(2**hb)-2,hb)
    i=0
    hh[-1]='0'
    for j in range(1,(2**nb)+1):
        for g in range(2**hb):
            m.append('.'.join(hh))
            i+=1
            hh[-1]=str(i)
            if i==256:
                ls[-2]=ls[-2]+1
                hh[-2]=str(ls[-2])
                i=0
            if ls[-2]==256:
                ls[-3]=ls[-3]+1
                hh[-3]=str(ls[-3])
                ls[-2]=0
        print("Network :",j)        
        print("Network ID :",m[0])
        print("Broadcast ID :",m[-1])
        print("usable ip's :",m[1],"-",m[-2])
        main.append(m)
        m=[]
        

elif int(ip_address[0])>=192 and int(ip_address[0])<=223:
    p=24
    print("class")
    nb=pre_len-p
    hb=32-pre_len
    print("No.of Networks :",2**nb,nb)
    print("No.of Host :",(2**hb)-2,hb)
    i=0
    hh[-1]='0'
    for j in range(1,(2**nb)+1):
        for g in range(2**hb):
            m.append('.'.join(hh))
            i+=1
            hh[-1]=str(i)
            if i==256:
                ls[-2]=ls[-2]+1
                hh[-2]=str(ls[-2])
                i=0
            if ls[-2]==256:
                ls[-3]=ls[-3]+1
                hh[-3]=str(ls[-3])
                ls[-2]=0
        print("Network :",j)        
        print("Network ID :",m[0])
        print("Broadcast ID :",m[-1])
        print("usable ip's :",m[1],"-",m[-2])
        main.append(m)
        m=[]
        

    

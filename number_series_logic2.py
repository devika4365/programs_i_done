num=int(input())
main=[1]
sub=[1]
a=0
b=1
j=0
while len(main)<=num:
    c=a+b
    sub.append(c**2)
    r=sub[j]+main[j]
    main.append(r)
    a=b
    b=c
    j+=1
print(*main)    
    

n1,n2=map(int,input().split())
count=0
for i in range(n1,n2+1):
    k=n1
    rev=0
    while n1>0:
        r=n1%10
        n1=n1//10
        rev=rev*10+r
    if rev==k:
        count+=1
print(count)        
        
        

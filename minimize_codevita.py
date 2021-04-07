m,k=map(int,input().split())
l=list(map(int,input().split()))
for j in range(k):
  d=l.index(max(l))
  l[d]=int(max(l)/2)
print(sum(l),end='')  
  

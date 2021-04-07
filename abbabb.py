s=input()
e=list(set(s))
for i in s:
    if s.count(i)>=2 and i in e:
        e.remove(i)
if e==[]:
    print("possible")
else:
    print("impossible")

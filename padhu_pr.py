x=(4+2*4/2)
print(x,'4+2*4/2')
x=((4+2)*4/2)
print(x,'(4+2)*4/2')
x=(4+2*4-2)
print(x,"4+2*4-2")
x=((4+2)*4-2)
print(x,'(4+2)*4-2')
x=(4-2*2+6//3)
print(x,"4-2*2+6//3")
x=4-(2*2)+6//3
print(x,"4-(2*2)+6//3")
print(2**3**2)
print(x)
print((2**3)**2)
print(x)
print(5*2//3)
print(x)
print(5*(2//3))
print(x)
print("and,or in these both which is high precedence:")
x="sri"
y=0
if x=="sri" or x=="jaya" : #and y>=2:
    print("or is higher precedence")
else:
    print("and is higher precedence")
x="sri"
y=0
if (x=="sri" or x=="jaya") and y>=2:
    print("or is higher precedence")
else:
    print("and higher precedence")

s=input()
st=[]
org=[]
#{([])}[]
for i in range(len(s)):
    if ord(s[i])==40 or ord(s[i])==91 or ord(s[i])==123:
        st.append(s[i])
        print(s)
    else:
        if ord(s[i])==41  and ord(st[-1])==40:
            org.append(st.pop())
            org.append(s[i])
        elif ord(s[i])==93 and ord (st[-1])==91:
            org.append(st.pop())
            org.append(s[i])
        elif ord(s[i])==125 and ord(st[-1])==123:
            org.append(st.pop())
            org.append(s[i])
        else:
            break
if len(st)==0:
    print(len(st))
else:
    print(len(st)+1+len(org))
        
            
            

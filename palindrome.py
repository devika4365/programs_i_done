n=int(input("Enter number")) #integer input
m=n
# stores actual input
rev=0
# store reverse of number
while n>0:
    r=n%10
    # to extract last digit from number
    n=n//10
    #to find coefficient of number when number divided by 10
    rev=rev*10+r
    #last digit is added to form reverse of the number
if rev==m:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

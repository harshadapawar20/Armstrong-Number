n = int(input("Enter the number: "))
t = n
a = 0 
while(n!=0):
    rem = n%10
    a = a+(rem*rem*rem)
    n=n//10
if(a==t):
    print("Armstrong")

else:
    print("Not Armstrong")

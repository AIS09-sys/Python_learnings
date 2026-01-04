n=int(input("enter a number"))
temp=n
rev=0
while(temp>0):
    rem=temp%10
    rev=rev*10+rem#this reverse the number
    temp=temp//10
if(n == rev):
    print(f"{n}:{rev} is palindrome")
if(n !=rev):
    print(f"{n}:{rev} is normal number")